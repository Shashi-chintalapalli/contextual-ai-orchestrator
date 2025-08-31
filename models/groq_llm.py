from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
DEFAULT_MODEL = "llama-3.1-8b-instant"

def get_llm(model_name: str = DEFAULT_MODEL):
    """
    Returns a callable GROQ LLM wrapper.
    """
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY not found in environment variables.")
    
    client = Groq(api_key=GROQ_API_KEY)

    def invoke(prompt: str):
        response = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    return invoke
