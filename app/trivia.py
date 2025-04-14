class Question:
    def __init__(self, description, options, correct_answer, difficulty):
        self.description = description
        self.options = options
        self.correct_answer = correct_answer
        self.difficulty = difficulty

    def is_correct(self, answer):
        return self.correct_answer == answer

class Quiz:
    def __init__(self, easy_questions, medium_questions, hard_questions):
        self.questions = []
        self.current_question_index = 0

        self.difficulty = 'media' # Atributo para la dificultad actual del quiz

        self.questions_answered = 0 # Atributo para contar las preguntas respondidas

        self.correct_answers = 0
        self.correct_streak = 0 # Racha actual de respuestas correctas
        self.max_correct_streak = 0  # Máxima racha de respuestas correctas
        self.correct_streak_counter = 0 # Contador de racha de respuestas correctas (si llega a 2, sube la dificultad)

        self.incorrect_answers = 0
        self.incorrect_streak = 0 # Racha actual de respuestas incorrectas
        self.incorrect_streak_counter = 0 # Contador de racha de respuestas incorrectas (si llega a 2, baja la dificultad)

        # Inicializamos las preguntas de cada dificultad
        self.easy_questions = easy_questions.copy()
        self.medium_questions = medium_questions.copy()
        self.hard_questions = hard_questions.copy()


    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        difficulty = self.difficulty

        if difficulty == 'facil':
            new_question = self.easy_questions.pop() 
        elif difficulty == 'media':
            new_question = self.medium_questions.pop()
        elif difficulty == 'dificil':
            new_question = self.hard_questions.pop()

        # Añadir la nueva pregunta a la lista de preguntas
        self.add_question(new_question)

        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None

    def answer_question(self,question, answer):
        self.questions_answered += 1 # Contamos esta pregunta como respondida

        if question.is_correct(answer):
            self.correct_answers += 1
            return True
        else:
            self.incorrect_answers += 1
            return False

def run_quiz():
    print("=" * 80)
    ascii_art = """
   ▄▄▄▄▀ █▄▄▄▄ ▄█     ▄   ▄█ ██   
▀▀▀ █    █  ▄▀ ██      █  ██ █ █  
    █    █▀▀▌  ██ █     █ ██ █▄▄█ 
   █     █  █  ▐█  █    █ ▐█ █  █ 
  ▀        █    ▐   █  █   ▐    █ 
          ▀          █▐        █  
                     ▐        ▀    
"""

    print(ascii_art)

    print("BIENVENIDO AL JUEGO DE TRIVIA!\n")
    print("Responde las siguientes preguntas seleccionando el número de la opción correcta.\n")
    print("Consideraciones:")
    print("1. Si no quieres responder una pregunta, puedes escribir '0' para saltarla.")
    print("2. Si quieres salir del juego, puedes escribir 'q' en cualquier momento.")
    print("=" * 80)
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
        if not question:
            print("No hay más preguntas disponibles.")
            break

        print(f"Pregunta {quiz.current_question_index}: {question.description}")
        for idx, option in enumerate(question.options):
            print(f"{idx + 1}) {option}")

        # Espera la respuesta del usuario y valida la entrada
        while True:
            try:
                option_idx = input("Selecciona una opción (1-4): ")
                # Verificamos si la respuesta está en uno de estos 3 casos
                if (option_idx.lower() == 'q') or (int(option_idx) == 0) or (1 <= int(option_idx) <= 4): 
                    break
                else:
                    print("Opción no válida. Intenta de nuevo.")
            except ValueError:
                print("Entrada no válida. Por favor, ingresa un número.")
        
        # Si el usuario quiere saltar la pregunta
        if option_idx == '0':
            print("Pregunta saltada.\n")
            continue

        # Si el usuario quiere salir del juego
        if option_idx == 'q':
            print("Saliendo del juego...\n")
            show_results(quiz)
            return

        # Capturamos la opción seleccionada
        option_idx = int(option_idx)
        answer = question.options[option_idx - 1]

        # Verificamos si la respuesta es correcta
        if quiz.answer_question(question, answer):
            print("¡Respuesta correcta!\n")
        else:
            print(f"Respuesta incorrecta. La respuesta correcta era: {question.correct_answer}\n")

    print("Juego terminado.")
    show_results(quiz)

# Función para mostrar los resultados finales
def show_results(quiz):
    print("Resultados del juego:")
    print(f"Preguntas contestadas: {quiz.questions_answered}")
    print(f"Respuestas correctas: {quiz.correct_answers}")
    print(f"Respuestas incorrectas: {quiz.incorrect_answers}")

if __name__ == "__main__":
    run_quiz()
