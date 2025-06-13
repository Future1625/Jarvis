from dotenv import load_dotenv
import os

load_dotenv()  # loads variables from .env into environment

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
WAKE_WORD = os.getenv("WAKE_WORD", "jarvis")  # fallback default
