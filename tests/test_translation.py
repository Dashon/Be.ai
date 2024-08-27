from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_translate():
    response = client.post(
        "/translate/",
        json={
            "text": "Hello, how are you?",
            "source_lang": "en",
            "target_lang": "aave",
        },
    )
    assert response.status_code == 200
    assert "translated_text" in response.json()
