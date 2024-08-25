import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
class Config:
    OPENAI_API_KEY = os.environ.get('OPENAPI_KEY')
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')