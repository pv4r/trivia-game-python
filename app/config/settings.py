import os
from dotenv import load_dotenv

from pathlib import Path
# Ir dos niveles arriba desde settings.py (de config/ a app/, luego a raíz del proyecto)
BASE_DIR = Path(__file__).resolve().parent.parent.parent
env_path = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME:str = "trivia-game-python"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER : str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER","localhost")
    POSTGRES_PORT : str = os.getenv("POSTGRES_PORT",5432) 
    POSTGRES_DB : str = os.getenv("POSTGRES_DB","tdd")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

settings = Settings()
