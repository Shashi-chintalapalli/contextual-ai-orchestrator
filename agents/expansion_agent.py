from models.groq_llm import get_llm

def expand_outline(outline: list[str], summary: str, mode: str = "short") -> list[str]:
    llm = get_llm()
    expanded_slides = []

    for slide in outline:
        prompt = (
            f"You are a presentation writer. Based on the following summary:\n\n{summary}\n\n"
            f"Expand this slide into short, clear content:\n{slide}\n\n"
            "Respond with 3–5 bullet points or a brief paragraph (max 50 words). Keep it concise and presentation-friendly."
        )

        # Optional: shorten prompt if mode is "short"
        if mode == "short":
            prompt += "\nKeep it ultra concise. Focus on clarity over detail."

        response = llm(prompt)
        expanded_slides.append(response.strip())

    return expanded_slides
