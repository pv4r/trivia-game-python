from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config.settings import settings


SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL # "postgresql://user:password@postgresserver/db"
engine = create_engine(SQLALCHEMY_DATABASE_URL) # Creacion del motor de la base de datos

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine) # Creacion de la session de la base de datos

# Retorna una session de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
