from pydantic import BaseModel


class JokeResponse(BaseModel):
    joke: str
