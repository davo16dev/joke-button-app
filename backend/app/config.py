import os

JOKE_API_URL = os.getenv(
    "JOKE_API_URL", "https://v2.jokeapi.dev/joke/Programming?type=single")
