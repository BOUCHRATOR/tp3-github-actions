
import pytest
from app.web import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


# Test 1 : message normal
def test_message_normal(client):
    response = client.post(
        "/moderate",
        json={"message": "bonjour"}
    )

    assert response.status_code == 200
    assert response.get_json() == {"decision": "autoriser"}


# Test 2 : message contenant SPAM
def test_message_spam(client):
    response = client.post(
        "/moderate",
        json={"message": "ceci est du SPAM"}
    )

    assert response.status_code == 200
    assert response.get_json() == {"decision": "bloquer"}


# Test 3 : message vide (objet JSON vide)
def test_message_absent(client):
    response = client.post(
        "/moderate",
        json={}
    )

    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid message"}


# Test 4 : message avec un nombre
def test_message_nombre(client):
    response = client.post(
        "/moderate",
        json={"message": 42}
    )

    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid message"}


# Bonus 1 : message composé d'espaces
def test_message_espaces(client):
    response = client.post(
        "/moderate",
        json={"message": "   "}
    )

    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid message"}


# Bonus 2 : corps JSON de type liste
def test_json_liste(client):
    response = client.post(
        "/moderate",
        json=["bonjour", "spam"]
    )

    assert response.status_code == 400
    assert response.get_json() == {"error": "JSON object required"}
