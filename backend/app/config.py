from pydantic import BaseModel
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv() # loads variables from .env if present

class Settings(BaseModel):
    db_url: str = os.getenv("DB_URL", "sqlite:///./app.db")
    upload_dir: str = os.getenv("UPLOAD_DIR", "./uploads")
    cors_origins: list[str] = os.getenv(
        "CORS_ORIGINS",
        "http://localhost:5173"
    ).split(",")

settings = Settings()

# Ensure upload directory exists
Path(settings.upload_dir).mkdir(parents=True, exist_ok=True)