from sqlalchemy import Column, Integer, String, JSON, Enum

from app.config.base_class import Base

# Definimos el modelo de la tabla de preguntas
class DBQuestion(Base):
    __tablename__ = 'questions' # Sobreescribimos el nombre de la tabla
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    options = Column(JSON)
    correct_answer = Column(String, nullable=False)
    # Utilizamos el enum (creado en la base de datos) para definir los niveles de dificultad
    difficulty = Column(Enum('facil', 'media', 'dificil', name='difficulty_level', create_type=False))



