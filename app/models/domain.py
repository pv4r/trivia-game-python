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

