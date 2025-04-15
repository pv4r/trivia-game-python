from app.services.quiz_service import QuizService
from app.services.question_service import QuestionService
from app.repositories.question_repository import QuestionRepository
from app.config.session import get_db
from app.models.domain import Quiz

def run_quiz():
    # Setup de dependencias
    db = next(get_db())
    question_repo = QuestionRepository(db)
    question_service = QuestionService(question_repo)
    quiz_service = QuizService(question_service)
    
    # Inicializar quiz
    quiz = quiz_service.initialize_quiz()
    
    # Mostrar la introducción del juego (banner y consideraciones)
    print("=" * 60)
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
    print("BIENVENIDO AL JUEGO!\n")
    print("Responde las siguientes preguntas seleccionando el número de la opción correcta.\n")
    print("Consideraciones:")
    print("1. Si no quieres responder una pregunta, puedes escribir '0' para saltarla.")
    print("2. Si quieres salir del juego, puedes escribir 'q' en cualquier momento.")
    print("=" * 60)
    print()

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

        # Si ya estamos en la última pregunta, no ajustamos la dificultad
        if quiz.current_question_index == 10:
            break

        # Ajustamos la dificultad según la racha de respuestas correctas o incorrectas
        if quiz.correct_streak_counter >= 2 and quiz.difficulty != 'dificil':
            quiz.adjust_difficulty("up")
            print(f"¡Has subido de dificultad! Ahora es {quiz.difficulty}.\n")
        elif quiz.incorrect_streak_counter >= 2 and quiz.difficulty != 'facil':
            quiz.adjust_difficulty("down")
            print(f"¡Has bajado de dificultad! Ahora es {quiz.difficulty}.\n")

    print("Juego terminado.")
    show_results(quiz)

# Función para mostrar los resultados finales
def show_results(quiz: Quiz):
    print("Resultados del juego:")
    print(f"Preguntas contestadas: {quiz.questions_answered}")
    print(f"Respuestas correctas: {quiz.correct_answers}")
    print(f"Respuestas incorrectas: {quiz.incorrect_answers}")
    print(f"Máxima racha de respuestas correctas: {quiz.max_correct_streak}")

if __name__ == "__main__":
    run_quiz()
