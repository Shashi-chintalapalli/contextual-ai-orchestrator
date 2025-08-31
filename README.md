# 🧠 AI Presentation Generator

Generate concise, context-aware PowerPoint presentations from uploaded documents using FastAPI, LangChain, and Groq LLM.

![screenshot]
---

## 🚀 Features

- 📄 Upload `.pdf`, `.docx`, or `.txt` files
- 🧠 Summarize content using Groq LLM + LangChain
- 🎯 Choose between short (6–7 slides) or full (10–15 slides) modes
- 🎨 Warm-themed, responsive UI built with HTML/CSS
- ⚡ FastAPI backend with modular orchestration
- 🔐 Secure environment management via `.env`

---

## 🛠️ Tech Stack

| Layer       | Tools Used                          |
|-------------|-------------------------------------|
| Backend     | FastAPI, LangChain, Groq            |
| Frontend    | HTML, CSS (warm theme)              |
| Parsing     | PyMuPDF, python-docx, chardet       |
| Slide Gen   | python-pptx                         |
| Security    | python-dotenv, MIME validation      |
| Deployment  | Docker, Render                      |

---

## 📦 Setup

### 1. Clone the repo


git clone https://github.com/your-username/ai-presentation-generator.git
cd ai-presentation-generator


## Add your .env

GROQ_API_KEY=your_groq_key
FILE_UPLOAD_DIR=/app/uploads


## Build & Run with Docker
docker build -t ai-ppt-generator .
docker run -p 8000:8000 ai-ppt-generator


## File Structure
/app
├── main.py
├── routes/
│   └── presentation.py
├── templates/
│   └── home.html
├── uploads/
├── requirements.txt
├── Dockerfile
└── .env.example
