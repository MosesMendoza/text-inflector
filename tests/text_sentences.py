from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_post_sentences_returns_sentences():
  text = "I am a pear. No, you're an apple. And not just any apple."
  response = client.post(
    "/sentences",
    json={
      "text": text
    }
  )
  assert response.json()["sentences"] == ["I am a pear.", "No, you're an apple.", "And not just any apple."]

def test_post_empty_string_to_sentences_returns_empty_sentences():
  text = ""
  response = client.post(
    "/sentences",
    json={
      "text": text
    }
  )
  assert response.json()["sentences"] == []

def test_post_tokenizations_without_body_returns_422():
  response = client.post(
    "/sentences"
  )
  assert response.status_code == 422

def test_post_tokenizations_without_text_field_returns_422():
  response = client.post(
    "/sentences",
    json={}
  )
  assert response.status_code == 422


def test_get_tokenizations_returns_405():
  response = client.get("/sentences")
  assert response.status_code == 405