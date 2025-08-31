# 📍 File: presentation_pipeline.py

from utils.file_loader import load_document
from utils.preprocess import chunk_document
from agents.analyzer_agent import analyze_document
from agents.decision_agent import decide_presentation_type
from agents.outline_agent import generate_outline
from agents.expansion_agent import expand_outline
from agents.pptx_agent import build_presentation, save_presentation

def run_presentation_pipeline(doc_path: str, output_pptx: str = "generated_presentation.pptx"):
    # 📥 Step 1: Load and chunk document
    documents = load_document(doc_path)
    chunks = chunk_document(documents)

    # 🧠 Step 2: Analyze and summarize
    summary = analyze_document(chunks)

    # 🎯 Step 3: Decide presentation type
    presentation_type = decide_presentation_type(summary)

    # 🗂️ Step 4: Generate outline
    outline = generate_outline(presentation_type, summary)

    # 📈 Step 5: Expand each slide
    expanded_slides = expand_outline(outline, summary)

    # 🎨 Step 6: Build and save presentation
    presentation = build_presentation(outline, summary)
    save_presentation(presentation, output_pptx)

    print(f"✅ Presentation generated: {output_pptx}")
