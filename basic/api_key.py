import os

from agents import set_tracing_export_api_key
from dotenv import load_dotenv

def ensure_api_key():
    load_dotenv(override=True)
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if not openai_api_key:
        print("No OpenAI API key has been found. Rename .env.template to .env and add put your key in there.")
    else:
        set_tracing_export_api_key(os.getenv("OPENAI_API_KEY"))
        print("OpenAI API key has been configured.")