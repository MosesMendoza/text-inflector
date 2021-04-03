from fastapi import APIRouter
from textblob import TextBlob
from ..models.document import Document

router = APIRouter()

@router.post("/tags", tags=["users"])
async def getTags(document: Document):
  text = document.text
  txtObj = TextBlob(text)
  tags = txtObj.tags
  return {"tags": tags}
