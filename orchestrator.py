from agents.pdf_ingestor import extract_text_from_pdf
from agents.outline_expander import expand_slide
from agents.pptx_agent import create_slide, save_presentation
from pptx import Presentation

# 📥 Step 1: Ingest PDF
pdf_path = "/Users/shashichintalapalli/Documents/SHASHI_DATA_3Y.pdf"
raw_text = extract_text_from_pdf(pdf_path)

# 🧠 Step 2: Generate outline (simple logic — replace with LLM later)
outline = [line.strip() for line in raw_text.split("\n") if line.strip()]
outline = outline[:5]  # First 5 lines as slide titles
summary = raw_text[:500] + "..."

# 🎨 Step 3: Build presentation
prs = Presentation()
for section in outline:
    content = expand_slide(section, summary)
    create_slide(prs, section, content)

# 💾 Step 4: Save and open
save_presentation(prs, "pipeline_output.pptx")
