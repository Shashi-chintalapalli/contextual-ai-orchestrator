from models.groq_llm import get_llm
from langchain.docstore.document import Document
from typing import List

def analyze_document(chunks: List[Document]) -> str:
    llm = get_llm()
    combined_text = "\n".join([doc.page_content for doc in chunks])
    
    prompt = (
        "You are an expert analyst. Read the following document and summarize its key themes, "
        "insights, and purpose in a concise, structured format:\n\n"
        f"{combined_text}"
    )
    
    return llm(prompt)
