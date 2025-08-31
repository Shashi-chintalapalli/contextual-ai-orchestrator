import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def expand_slide(section_title, summary):

    prompt = f"""
You are an expert AI presentation assistant. Expand the following slide title into detailed content suitable for a professional presentation. Use clear, informative language. Avoid fluff.

Slide Title: "{section_title}"
Presentation Summary: "{summary}"

Respond with a concise paragraph or bullet points.
"""

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mixtral-8x7b-32768",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=payload)
    response.raise_for_status()
    content = response.json()["choices"][0]["message"]["content"]
    return content.strip()
