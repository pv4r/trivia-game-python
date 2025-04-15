## [Unreleased]
### Added
- cb52ff0: Estructura base del proyecto según la recomendación oficial de FastAPI.
- dda4af0: Archivos de configuración para contenedores: `Dockerfile` y `docker-compose.yml`.
- b6f0d29: Archivo `.gitignore` generado para entorno Python + Docker.

## [Unreleased]
### Changed
- 4894c26: Se agrego paquete pytest a `requirements.txt` para pruebas unitarias.
### Added
- 3a998d1: Creacion de la clase `Question` en `trivia.py` para representar una pregunta de trivia, junto con la prueba unitaria correspondiente.

## [Unreleased]
### Changed
- f567a52: Se corrigio el problema del import de `trivia` dentro de `test_trivia.py`
### Added
- 8e7c646: Creacion de la clase Quiz en `trivia.py`
- de275a6: Creacion de la funcion `run_quiz` en `trivia.py`

## [Unreleased]
### Added
- a2a4dc1: Se agrego un test para validar el sistema de puntuacion
- 4126959: Se definio la logica para las 10 rondas
- bf4ac97: Implementacion del método `answer_question` en la clase Quiz
- a28aeba: Se incluyeron los atributos `correct_answers` e `incorrect_answers` en la clase Quiz

## [Unreleased]
### Changed
- 04fc589: Mejora en la presentación de las preguntas y respuestas en la consola. Se agrego un banner de bienvenida, usando ascii art.
- 15137bb: Cambio a `get_next_question` para que utilice los nuevos atributos de dificultad.
- f8b8465: Cambio a `answer_question` para que maneje el conteo de rachas.
- 6ae0d0e: Arreglos al banner
### Added
- 54307a2: Se agregaron atributos a la clase `Question` y `Quiz` para manejar la dificultad de las preguntas.
- f8b8465: Se creo la funcion `adjust_difficult` para ajustar la dificultad del quiz.
- 8648252: Creacion de 3 listas de preguntas para cada nivel de dificultad.
- 987393f: Se integraron los cambios de dificultad segun la racha de respuestas.
- 53a9504: Nueva linea que muestra la maxima racha de preguntas correctas.
- 17e2ba8: Solucion al cambio de dificultad en la ultima pregunta.

## [Unreleased]
### Changed
- b5a7797: Se elimina el archivo `app/trivia.py` para mover se logica a un submodulo
- d94f2af: Se agrego healthcheck para db y se creo el servicio quiz para poder ejecutarlo despues
- 40921e0: Se importan los settings para crear la aplicacion
### Added
- 0502fde: Se agrego el paquete psycopg2-binary debido a que sqlalchemy lo necesita como driver
- 7c7fe50: (Nueva estructura) Creacion de los modulos config,entrypoints, entrypoints/cli, models, repositories, services para mejor distribucion de las funcionalidades
- 3aeb512: Creacion del archivo `settings.py` para manejar las variables de la aplicacion
- 6dfb16d: Creacion de session.py para crear la sesion de la base de datos y retornarla
- 8d00515: Creacion de `base_class.py` que contiene la clase base para los modelos de SQLAlchemy
- 1a075a5: Creacion de `db_models.py` para manejar el modelo de la tabla de preguntas
- 81f3c0f: Creacion de `domain.py` que ahora contiene las clases `Question` y `Quiz`
- f4a60cc: Creacion de `question_repository.py` junto con la clase `QuestionRepository`
- a81fd9f: Creacion de `question_service.py` con la clase `QuestionService`
- 15959bd: Creacion de `quiz_service.py` con la clase `QuizService`
- 8d25acc: Creacion de `run_quiz.py` que contiene la logica de ejecucion del juego


