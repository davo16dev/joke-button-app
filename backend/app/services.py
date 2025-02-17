import requests
from typing import Optional

from app.config import JOKE_API_URL


def get_random_joke_from_joke_api() -> Optional[str]:
    """
    Fetches a random joke from the Joke API.

    Logs the response and raises an exception if the request fails.

    Returns:
        str | None: The joke if found, otherwise None.
    """
    response = requests.get(JOKE_API_URL, timeout=5)
    import logging
    logging.warning(response)
    response.raise_for_status()
    data = response.json()
    return data.get("joke", None)
