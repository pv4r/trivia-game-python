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
            self.correct_streak += 1
            self.correct_streak_counter += 1
            self.max_correct_streak = max(self.max_correct_streak, self.correct_streak) # Actualizar la máxima racha

            self.incorrect_streak = 0
            self.incorrect_streak_counter = 0

            return True
        else:
            self.incorrect_answers += 1
            self.incorrect_streak += 1
            self.incorrect_streak_counter += 1

            self.correct_streak = 0
            self.correct_streak_counter = 0

            return False

    def adjust_difficulty(self, direction):
        if direction == "up":
            if self.difficulty == 'facil': # Cambio a dificultad 'media'
                self.difficulty = 'media'
            elif self.difficulty == 'media': # Cambio a dificultad 'dificil'
                self.difficulty = 'dificil'
            self.correct_streak_counter = 0 # Resetear el contador de racha

        elif direction == "down":
            if self.difficulty == 'dificil': # Cambio a dificultad 'media'
                self.difficulty = 'media'
            elif self.difficulty == 'media': # Cambio a dificultad 'facil'
                self.difficulty = 'facil'
            self.incorrect_streak_counter = 0 # Resetear el contador de racha

def run_quiz():
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

    # Listas de preguntas por dificultad
    easy_questions = []
    medium_questions = []
    hard_questions = []

    # Añadir preguntas faciles
    easy_questions = [
        Question("¿Cuál es la capital de Francia?", ["Berlin", "Madrid", "Paris", "Roma"], "Paris", 'facil'),
        Question("¿Cuántos lados tiene un triangulo?", ["2", "3", "4", "5"], "3", 'facil'),
        Question("¿Cuál es el color del cielo en un dia despejado?", ["Rojo", "Verde", "Azul", "Amarillo"], "Azul", 'facil'),
        Question("¿Qué animal dice 'miau'?", ["Perro", "Gato", "Vaca", "Pajaro"], "Gato", 'facil'),
        Question("¿Cuál es el resultado de 2+2?", ["3", "4", "5", "6"], "4", 'facil'),
        Question("¿Cuál es el oceano mas grande?", ["Atlantico", "Indico", "Pacifico", "Artico"], "Pacifico", 'facil'),
        Question("¿Qué planeta es conocido como el planeta rojo?", ["Venus", "Marte", "Jupiter", "Saturno"], "Marte", 'facil'),
        Question("¿Cuál es el metal mas usado en cables electricos?", ["Oro", "Plata", "Cobre", "Aluminio"], "Cobre", 'facil'),
        Question("¿Cuántos dias tiene una semana?", ["5", "6", "7", "8"], "7", 'facil'),
        Question("¿Qué instrumento tiene cuerdas y se toca con arco?", ["Guitarra", "Violin", "Piano", "Tambor"], "Violin", 'facil'),
        Question("¿Cuál es el pais mas grande del mundo?", ["Canada", "China", "Rusia", "EEUU"], "Rusia", 'facil'),
        Question("¿Qué gas necesitan las plantas para la fotosintesis?", ["Oxigeno", "Nitrogeno", "Dioxido de carbono", "Hidrogeno"], "Dioxido de carbono", 'facil'),
        Question("¿Cuál es la capital de Canada?", ["Toronto", "Ottawa", "Vancouver", "Montreal"], "Ottawa", 'facil'),
        Question("¿Qué planeta es el mas cercano al Sol?", ["Venus", "Tierra", "Marte", "Mercurio"], "Mercurio", 'facil'),
        Question("¿Cuál es el hueso mas largo del cuerpo humano?", ["Costilla", "Esternon", "Femur", "Humero"], "Femur", 'facil'),
        Question("¿Qué pais tiene forma de bota?", ["Francia", "Espana", "Italia", "Portugal"], "Italia", 'facil'),
        Question("¿Cuántos continentes hay en el mundo?", ["5", "6", "7", "8"], "7", 'facil'),
        Question("¿Qué fruto seco se usa para hacer mantequilla de mani?", ["Almendras", "Nueces", "Castañas", "Manies"], "Manies", 'facil'),
        Question("¿Cuál es el simbolo quimico del oro?", ["Go", "Au", "Ag", "Gd"], "Au", 'facil'),
        Question("¿Qué deporte juega Lionel Messi?", ["Tenis", "Futbol", "Baloncesto", "Golf"], "Futbol", 'facil')
    ]

    # Añadir preguntas medias
    medium_questions = [
        Question("¿Cuál es el río más largo del mundo?", ["Nilo", "Amazonas", "Yangtse", "Misisipi"], "Amazonas", 'media'),
        Question("¿En qué año llegó el hombre a la Luna?", ["1965", "1969", "1972", "1981"], "1969", 'media'),
        Question("¿Cuál es el país con más husos horarios?", ["Rusia", "Francia", "EEUU", "China"], "Francia", 'media'),
        Question("¿Qué científico formuló la teoría de la relatividad?", ["Newton", "Einstein", "Tesla", "Hawking"], "Einstein", 'media'),
        Question("¿Cuál es el elemento químico más abundante en la Tierra?", ["Oxígeno", "Silicio", "Aluminio", "Hierro"], "Oxígeno", 'media'),
        Question("¿Qué país inventó el sushi?", ["China", "Tailandia", "Japón", "Corea"], "Japón", 'media'),
        Question("¿Cuál es la montaña más alta de África?", ["Monte Kenya", "Kilimanjaro", "Atlas", "Ruwenzori"], "Kilimanjaro", 'media'),
        Question("¿Qué escritor creó a Harry Potter?", ["J.R.R. Tolkien", "J.K. Rowling", "George R.R. Martin", "Stephen King"], "J.K. Rowling", 'media'),
        Question("¿Cuántos elementos tiene la tabla periódica?", ["118", "92", "150", "206"], "118", 'media'),
        Question("¿Qué lenguaje de programación creó Guido van Rossum?", ["Java", "Python", "C++", "JavaScript"], "Python", 'media'),
        Question("¿Cuál es la capital de Australia?", ["Sydney", "Melbourne", "Canberra", "Brisbane"], "Canberra", 'media'),
        Question("¿Qué planeta tiene anillos visibles?", ["Júpiter", "Saturno", "Urano", "Neptuno"], "Saturno", 'media'),
        Question("¿Cuál es el hueso más pequeño del cuerpo humano?", ["Estribo", "Martillo", "Yunque", "Falange"], "Estribo", 'media'),
        Question("¿Qué país no es parte de la Unión Europea?", ["Noruega", "Alemania", "Francia", "Italia"], "Noruega", 'media'),
        Question("¿Cuál es el animal terrestre más rápido?", ["León", "Guepardo", "Antílope", "Caballo"], "Guepardo", 'media'),
        Question("¿Qué pintor cortó su propia oreja?", ["Picasso", "Van Gogh", "Dalí", "Monet"], "Van Gogh", 'media'),
        Question("¿Cuál es el órgano más grande del cuerpo humano?", ["Corazón", "Hígado", "Piel", "Cerebro"], "Piel", 'media'),
        Question("¿Qué país tiene la bandera roja con un círculo amarillo?", ["China", "Japón", "Vietnam", "Tailandia"], "Japón", 'media'),
        Question("¿Cuál es el metal líquido a temperatura ambiente?", ["Plomo", "Mercurio", "Bromo", "Cesio"], "Mercurio", 'media'),
        Question("¿Qué planeta tiene la rotación más rápida?", ["Júpiter", "Saturno", "Venus", "Mercurio"], "Júpiter", 'media')
    ]

    # Añadir preguntas difíciles
    hard_questions = [
        Question("¿Cuál es el punto más profundo del océano?", ["Fosa de las Marianas", "Fosa de Tonga", "Fosa de Puerto Rico", "Fosa de Java"], "Fosa de las Marianas", 'dificil'),
        Question("¿Qué científico descubrió la penicilina?", ["Marie Curie", "Alexander Fleming", "Louis Pasteur", "Robert Koch"], "Alexander Fleming", 'dificil'),
        Question("¿Cuál es el país con más islas en el mundo?", ["Filipinas", "Indonesia", "Suecia", "Canadá"], "Suecia", 'dificil'),
        Question("¿Qué elemento tiene el símbolo químico 'W'?", ["Tungsteno", "Wolframio", "Oro blanco", "Platino"], "Tungsteno", 'dificil'),
        Question("¿Cuál es el libro más vendido de la historia?", ["Don Quijote", "La Biblia", "El Señor de los Anillos", "Harry Potter"], "La Biblia", 'dificil'),
        Question("¿Qué país tiene la constitución escrita más antigua?", ["Francia", "EEUU", "Inglaterra", "Suiza"], "EEUU", 'dificil'),
        Question("¿Cuál es la velocidad de la luz en el vacío?", ["300,000 km/s", "150,000 km/s", "450,000 km/s", "600,000 km/s"], "300,000 km/s", 'dificil'),
        Question("¿Qué planeta tiene el día más largo?", ["Venus", "Mercurio", "Júpiter", "Neptuno"], "Venus", 'dificil'),
        Question("¿Cuál es el único mamífero capaz de volar?", ["Ave", "Murciélago", "Ardilla voladora", "Colugo"], "Murciélago", 'dificil'),
        Question("¿Qué país tiene tres capitales?", ["Sudáfrica", "Chile", "Australia", "Rusia"], "Sudáfrica", 'dificil'),
        Question("¿Cuál es el lago más profundo del mundo?", ["Lago Superior", "Lago Baikal", "Lago Tanganica", "Lago Vostok"], "Lago Baikal", 'dificil'),
        Question("¿Qué lenguaje de programación fue creado por Bjarne Stroustrup?", ["Java", "C++", "Python", "C#"], "C++", 'dificil'),
        Question("¿Cuál es la ciudad más poblada del mundo?", ["Shanghái", "Tokio", "Delhi", "São Paulo"], "Tokio", 'dificil'),
        Question("¿Qué reina británica tuvo el reinado más largo?", ["Victoria", "Isabel I", "Isabel II", "Ana"], "Isabel II", 'dificil'),
        Question("¿Cuál es el hueso más duro del cuerpo humano?", ["Fémur", "Tibia", "Mandíbula", "Cráneo"], "Mandíbula", 'dificil'),
        Question("¿Qué país no tiene un río permanente?", ["Arabia Saudita", "Kuwait", "Qatar", "Emiratos Árabes"], "Arabia Saudita", 'dificil'),
        Question("¿Cuál es el único elemento líquido a temperatura ambiente?", ["Bromo", "Mercurio", "Galio", "Cesio"], "Bromo", 'dificil'),
        Question("¿Qué científico propuso las tres leyes del movimiento?", ["Einstein", "Newton", "Galileo", "Copérnico"], "Newton", 'dificil'),
        Question("¿Cuál es el único mamífero venenoso?", ["Ornitorrinco", "Equidna", "Musaraña", "Topo"], "Ornitorrinco", 'dificil'),
        Question("¿Qué país tiene la mayor biodiversidad del mundo?", ["Indonesia", "Brasil", "Colombia", "Ecuador"], "Brasil", 'dificil')
    ]

    # Creamos una instancia de Quiz con las preguntas
    quiz = Quiz(easy_questions, medium_questions, hard_questions)

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
def show_results(quiz):
    print("Resultados del juego:")
    print(f"Preguntas contestadas: {quiz.questions_answered}")
    print(f"Respuestas correctas: {quiz.correct_answers}")
    print(f"Respuestas incorrectas: {quiz.incorrect_answers}")

if __name__ == "__main__":
    run_quiz()
