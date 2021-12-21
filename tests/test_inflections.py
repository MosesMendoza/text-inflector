from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_post_inflect_returns_noun_word_form():
  text = "pear"
  tag = "NNS"
  response = client.post(
    "/inflections",
    json={
      "word": {
        "text": text,
      },
      "pos": {
        "tag": tag
      }
    }
  )
  assert response.json() == { "inflection": ["pears"] }

def test_post_inflect_returns_verb_word_form():
  text = "grandfather"
  tag = "VBG"
  response = client.post(
    "/inflections",
    json={
      "word": {
        "text": text,
      },
      "pos": {
        "tag": tag
      }
    }
  )
  assert response.json() == { "inflection": ["grandfathering"] }

def test_post_inflect_without_body_returns_422():
  response = client.post(
    "/inflections"
  )
  assert response.status_code == 422


def test_post_inflect_without_text_field_returns_422():
  response = client.post(
    "/inflections",
    json={}
  )
  assert response.status_code == 422


def test_get_inflect_returns_405():
  response = client.get("/inflections")
  assert response.status_code == 405

def get_status_returns_200():
  response = client.get("/status")
  assert response.status_code == 200
