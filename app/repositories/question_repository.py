from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.db_models import DBQuestion
from app.models.domain import Question

# Esta clase es responsable de INTERACTUAR con la base de datos para las preguntas
class QuestionRepository:
    def __init__(self, db: Session):
        self.db = db
    
    # Obtiene preguntas aleatorias de la base de datos según la dificultad
    def get_by_difficulty(self, difficulty: str, limit: int = 20) -> list[Question]:
        db_questions = self.db.query(DBQuestion)\
                           .filter(DBQuestion.difficulty == difficulty)\
                           .order_by(func.random())\
                           .limit(limit)\
                           .all()
        return [
            Question(
                description=q.description,
                options=q.options,
                correct_answer=q.correct_answer,
                difficulty=q.difficulty
            ) for q in db_questions
        ]
    
    # Crea una nueva pregunta en la base de datos
    def create_question(self, question: Question):
        db_question = DBQuestion(
            description=question.description,
            options=question.options,
            correct_answer=question.correct_answer,
            difficulty=question.difficulty
        )
        self.db.add(db_question)
        self.db.commit()
        self.db.refresh(db_question)
        return db_question
