from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_post_tags_returns_parts_of_speech():
  text = "I am a pear."
  response = client.post(
    "/tags",
    json={
      "text": text
    }
  )
  assert response.json() == {"tags": [["I", "PRP"], ["am", "VBP"], ["a", "DT"], ["pear", "NN"]]}

def test_post_tags_without_body_returns_422():
  response = client.post(
    "/tags"
  )
  assert response.status_code == 422


def test_post_tags_without_text_field_returns_422():
  response = client.post(
    "/tags",
    json={}
  )
  assert response.status_code == 422


def test_get_tags_returns_405():
  response = client.get("/tags")
  assert response.status_code == 405