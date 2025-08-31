from models.groq_llm import get_llm

def decide_presentation_type(summary: str) -> str:
    llm = get_llm()
    
    prompt = (
        "You are a presentation strategist. Based on the following summary, "
        "decide what type of presentation should be created. "
        "Choose from: portfolio, pitch deck, strategy report, case study, or educational overview.\n\n"
        f"{summary}\n\n"
        "Respond with only the presentation type."
    )
    
    return llm(prompt).strip().lower()
