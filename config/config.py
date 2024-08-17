import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    API_KEY = os.getenv("API_KEY")
    MODEL_NAME = "gemini-1.5-flash-latest"