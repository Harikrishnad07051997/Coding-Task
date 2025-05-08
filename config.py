import os
from dotenv import load_dotenv

load_dotenv()

def load_config():
    return {
        "HOST": os.getenv("APP_HOST", "0.0.0.0"),
        "PORT": int(os.getenv("APP_PORT", 8000)),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO")
    }