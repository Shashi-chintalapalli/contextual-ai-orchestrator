from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse, HTMLResponse
import os
from run_pipeline import run_pipeline

app = FastAPI()

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "output"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>AI Presentation Generator</title>
            <style>
                body {
                    font-family: 'Segoe UI', sans-serif;
                    background: #f4f6f8;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                    margin: 0;
                }
                h2 {
                    color: #333;
                    margin-bottom: 20px;
                }
                form {
                    background: white;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                    text-align: center;
                }
                input[type=file] {
                    padding: 10px;
                    border: 2px dashed #ccc;
                    border-radius: 5px;
                    width: 100%;
                    margin-bottom: 15px;
                }
                select, input[type=submit] {
                    padding: 10px;
                    margin-top: 10px;
                    width: 100%;
                    border-radius: 5px;
                    border: none;
                    background-color: #0078d4;
                    color: white;
                    font-weight: bold;
                    cursor: pointer;
                }
                select {
                    background-color: #f0f0f0;
                    color: #333;
                    border: 1px solid #ccc;
                }
                input[type=submit]:hover {
                    background-color: #005fa3;
                }
                .footer {
                    margin-top: 30px;
                    font-size: 0.9em;
                    color: #777;
                }
            </style>
        </head>
        <body>
            <h2>📄 AI Presentation Generator</h2>
            <form action="/generate" enctype="multipart/form-data" method="post">
                <input type="file" name="file" accept=".pdf,.docx,.txt" required><br>
                <select name="mode">
                    <option value="short">Short (6–7 slides)</option>
                    <option value="full">Full (10–15 slides)</option>
                </select><br>
                <input type="submit" value="Generate Presentation">
            </form>
            <div class="footer">Built with FastAPI + Groq LLM ⚡</div>
        </body>
    </html>
    """

@app.post("/generate")
async def generate(file: UploadFile = File(...), mode: str = Form("short")):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    output_path = os.path.join(OUTPUT_DIR, "generated_presentation.pptx")
    run_pipeline(file_path, output_path, mode=mode)  # pass mode to pipeline

    return FileResponse(
        output_path,
        media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation",
        filename="presentation.pptx"
    )