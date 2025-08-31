from fastapi import APIRouter, File, UploadFile, Form
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import os
from run_pipeline import run_pipeline

router = APIRouter()
templates = Jinja2Templates(directory="templates")

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "output"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@router.post("/generate")
async def generate(file: UploadFile = File(...), mode: str = Form("short")):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    output_path = os.path.join(OUTPUT_DIR, "generated_presentation.pptx")
    run_pipeline(file_path, output_path, mode=mode)

    return FileResponse(
        output_path,
        media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation",
        filename="presentation.pptx"
    )
