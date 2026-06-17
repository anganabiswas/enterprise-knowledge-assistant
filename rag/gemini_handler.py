import google.generativeai as genai
from config.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_answer(context, question):

    prompt = f"""
You are an Enterprise Knowledge Assistant.

Answer ONLY using the provided context.

Instructions:
- Answer only from the provided context.
- Give a complete explanation when information exists.
- Do not unnecessarily shorten the answer.
- Use headings and bullet points when useful.
- Explain concepts clearly and professionally.
- If the answer is not present in the context, say:
"This information is not available in the knowledge base."

Question:
{question}

Context:
{context}
"""

    response = model.generate_content(
        prompt
    )

    return response.text