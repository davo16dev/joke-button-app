from app import services
from app.schemas import JokeResponse


def get_joke_api_client() -> JokeResponse:
    """
    Fetches a random joke from the external API.

    Raises:
        ValueError: If no joke is found.

    Returns:
        JokeResponse: The joke fetched from the API.
    """
    joke = services.get_random_joke_from_joke_api()
    if not joke:
        raise ValueError("No joke found in API response")
    return JokeResponse(joke=joke)
