from fastapi import APIRouter
from textblob import TextBlob
from models import document

router = APIRouter()

@router.post("/tags", tags=["users"])
async def getTags(document: Document):
  text = document.text
  txtObj = TextBlob(text)
  tags = txtObj.tags
  return [{"document": tags}]
