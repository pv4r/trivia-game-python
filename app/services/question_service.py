from typing import List
from app.models.domain import Question
from app.repositories.question_repository import QuestionRepository

# Esta clase interactúa con el repositorio de preguntas y aplica la lógica de negocio
class QuestionService:
    def __init__(self, question_repo: QuestionRepository):
        self.question_repo = question_repo # Inicializa el repositorio de preguntas
    
    # Obtiene la lista de preguntas por dificultad
    def get_questions_by_difficulty(self, difficulty: str) -> List[Question]:
        return self.question_repo.get_by_difficulty(difficulty)
