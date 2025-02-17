import requests
from fastapi import APIRouter, HTTPException, status
from typing import Any

from app.deps import get_joke_api_client
from app.schemas import JokeResponse


router = APIRouter()


@router.get(
        "/joke",
        summary="Get a random joke",
        description=(
            "This endpoint fetches a random joke from the external joke API."
        ),
        response_model=JokeResponse

)
def get_joke() -> Any:
    """
    Fetches a joke from the Joke API.

    Raises:
        HTTPException:
            - 404 if no joke is found.
            - 503 if there is an issue connecting to the Joke API.

    Returns:
        Any: The joke fetched from the API.
    """
    try:
        return get_joke_api_client()
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Joke not found"
        )
    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Error connecting to Joke API: {str(e)}"
        )
