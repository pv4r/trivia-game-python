from fastapi import FastAPI
from app.config.settings import settings

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    return app


app = start_application()


@app.get("/")
def home():
    return {"msg":"Hello FastAPI🚀"}



