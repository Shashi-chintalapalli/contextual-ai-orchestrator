from utils.file_loader import load_document
from utils.preprocess import chunk_document
from vectorstore.vector_db import store_documents
from agents.analyzer_agent import analyze_document
from agents.decision_agent import decide_presentation_type
from agents.outline_agent import generate_outline
from agents.expansion_agent import expand_outline
from agents.pptx_agent import build_presentation, save_presentation

def run_pipeline(file_path: str, output_filename: str = "final_output.pptx", mode: str = "short"):
    print("📥 Loading document...")
    docs = load_document(file_path)

    print("🧼 Chunking document...")
    max_chunks = 10 if mode == "short" else 20
    chunks = chunk_document(docs, max_chunks=max_chunks)

    print("🧠 Storing chunks in vector DB...")
    store_documents(chunks)

    print("🔍 Analyzing document...")
    summary = analyze_document(chunks)

    print("📊 Deciding presentation type...")
    presentation_type = decide_presentation_type(summary)
    print(f"➡️ Presentation type: {presentation_type}")

    print("📝 Generating outline...")
    slide_count = 7 if mode == "short" else 12

    # Use preset fallback if short mode
    outline = generate_outline(presentation_type, summary, slide_count=slide_count)


    print("📈 Expanding outline...")
    expanded_slides = expand_outline(outline, summary, mode=mode)

    print("🎨 Building presentation...")
    prs = build_presentation(outline, summary, mode=mode)

    print("💾 Saving presentation...")
    save_presentation(prs, filename=output_filename)

    print("✅ Pipeline complete.")
