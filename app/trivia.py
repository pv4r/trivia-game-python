class Question:
    def __init__(self, description, options, correct_answer):
        self.description = description
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, answer):
        return self.correct_answer == answer

class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0

    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None

def run_quiz():
    print("Bienvenido al juego de Trivia!")
    print("Responde las siguientes preguntas seleccionando el número de la opción correcta.")
    print()
    quiz = Quiz()

    # Ejemplo de preguntas
    quiz.add_question(Question("¿Cuál es la capital de Francia?", ["Berlín", "Madrid", "París", "Roma"], "París"))
    quiz.add_question(Question("¿Cuál es el océano más grande del mundo?", ["Atlántico", "Índico", "Pacífico", "Ártico"], "Pacífico"))
    quiz.add_question(Question("¿Cuál es el continente más grande?", ["África", "Asia", "América", "Europa"], "Asia"))
    quiz.add_question(Question("¿Cuál es el país más poblado del mundo?", ["India", "Estados Unidos", "China", "Indonesia"], "China"))
    quiz.add_question(Question("¿Cuál es el idioma más hablado del mundo?", ["Inglés", "Español", "Mandarín", "Árabe"], "Mandarín"))
    quiz.add_question(Question("¿Cuál es el planeta más grande del sistema solar?", ["Tierra", "Júpiter", "Saturno", "Marte"], "Júpiter"))
    quiz.add_question(Question("¿Cuál es el metal más ligero?", ["Aluminio", "Litio", "Mercurio", "Plomo"], "Litio"))
    quiz.add_question(Question("¿Cuál es la capital de Japón?", ["Seúl", "Tokio", "Pekín", "Bangkok"], "Tokio"))
    quiz.add_question(Question("¿Cuál es el país más grande del mundo?", ["Canadá", "Rusia", "China", "Estados Unidos"], "Rusia"))
    quiz.add_question(Question("¿Cuál es la montaña más alta del mundo?", ["K2", "Everest", "Kilimanjaro", "Mont Blanc"], "Everest"))

    while quiz.current_question_index < 10:
        question = quiz.get_next_question()
        print(f"Pregunta {quiz.current_question_index}: {question.description}")
        for idx, option in enumerate(question.options):
            print(f"{idx + 1}) {option}")
            
        print()
    print("Juego terminado.")
    print(f"Preguntas contestadas: 0")
    print(f"Respuestas correctas: 0")
    print(f"Respuestas incorrectas: 0")

if __name__ == "__main__":
    run_quiz()
