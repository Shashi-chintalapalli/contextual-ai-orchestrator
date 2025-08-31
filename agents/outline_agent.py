from models.groq_llm import get_llm

def generate_outline(presentation_type: str, summary: str, slide_count: int = 7) -> list[str]:
    llm = get_llm()
    prompt = (
        f"You are a presentation designer. Based on the following summary, "
        f"generate a {presentation_type} presentation outline with {slide_count} slides. "
        f"Each slide should have a title and a short description.\n\n"
        f"Summary:\n{summary}\n\n"
        "Respond in this format:\nSlide 1: [Title] - [Description]\nSlide 2: ..."
    )
    response = llm(prompt)
    slides = [line.strip() for line in response.split("\n") if line.strip()]
    return slides[:slide_count]

