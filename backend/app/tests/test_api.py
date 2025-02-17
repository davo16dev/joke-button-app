import pytest
from fastapi.testclient import TestClient
from requests.exceptions import RequestException
from unittest.mock import patch

from app import services
from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


@patch.object(services, 'get_random_joke_from_joke_api')
def test_get_joke_return_200(get_joke, client):
    mock_joke = "This is a funny joke!"
    get_joke.return_value = mock_joke

    response = client.get("/joke")

    assert response.status_code == 200
    actual_response = response.json()
    except_response = {"joke": mock_joke}
    assert actual_response == except_response


@patch.object(services, 'get_random_joke_from_joke_api')
def test_get_joke_return_404_not_found(get_joke, client):
    get_joke.return_value = None

    response = client.get("/joke")

    assert response.status_code == 404
    actual_response = response.json()['detail']
    except_response = "Joke not found"
    assert actual_response == except_response


@patch.object(services, 'get_random_joke_from_joke_api')
def test_get_joke_return_503_service_unavailable(get_joke, client):
    get_joke.side_effect = RequestException("Service unavailable")

    response = client.get("/joke")

    assert response.status_code == 503
    actual_response = response.json()['detail']
    expected_response = "Error connecting to Joke API: Service unavailable"
    assert actual_response == expected_response
