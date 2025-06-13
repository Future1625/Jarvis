import openrouter
import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

openrouter.api_key = OPENROUTER_API_KEY

def generate_ai_response(prompt: str) -> str:
    try:
        response = openrouter.ChatCompletion.create(
            model="undi95/toppy-m-7b",
            messages=[{"role": "user", "content": prompt}],
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"AI error: {str(e)}"
