from fastapi.testclient import TestClient
from ..app.main import app

client = TestClient(app)

def test_post_tags():
  text = "I am a pear"
  response = client.post(
    "/tags",
    json={
      "text": text
    }
  )
  assert response.json() == {"tags": 'foo'}
