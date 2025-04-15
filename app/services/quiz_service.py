from app.models.domain import Quiz
from app.services.question_service import QuestionService

class QuizService:
    def __init__(self, question_service: QuestionService):
        self.question_service = question_service # Inicializa un servicio de preguntas
    
    def initialize_quiz(self) -> Quiz:
        # Utiliza el servicio de preguntas para obtener preguntas de diferentes niveles de dificultad
        easy = self.question_service.get_questions_by_difficulty("facil")
        medium = self.question_service.get_questions_by_difficulty("media")
        hard = self.question_service.get_questions_by_difficulty("dificil")
        return Quiz(easy, medium, hard) # Crea un nuevo objeto Quiz con las listas de preguntas obtenidas
