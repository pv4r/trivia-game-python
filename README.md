# Trivia Game
Este es un juego de trivia simple en Python. El juego presenta preguntas de opción múltiple y permite al jugador seleccionar una respuesta.

## Requisitos
- Docker

## Instalación y uso
- Clona el repositorio:
```bash
git clone https://github.com/pv4r/trivia-game-python.git
cd trivia-game-python
```

### Ejecutar el juego
- Usa docker compose para levantar la base de datos:
```bash
docker compose up -d db
```
- Luego, ejecuta el juego también con docker compose:
```bash
docker compose run --rm quiz
```



