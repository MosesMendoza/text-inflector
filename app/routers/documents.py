from fastapi import Body, APIRouter
from textblob import TextBlob
from lemminflect import getInflection
from ..models.document import Document, Word
from ..models.part_of_speech import PartOfSpeech

router = APIRouter()

@router.post("/tags", tags=["documents"])
async def postTags(document: Document):
  text = document.text
  txtObj = TextBlob(text)
  tags = txtObj.tags
  return { "tags": tags }

@router.post("/inflections", tags=["documents"])
async def postInflection(word: Word, pos: PartOfSpeech = Body(...)):
  text = word.text
  tag = pos.tag
  inflection = getInflection(text, tag)
  return { "inflection": inflection }

@router.post("/sentences", tags=["documents"])
async def postInflection(document: Document):
  text = document.text
  txtObj = TextBlob(text)
  sentences = []
  for sentence in txtObj.sentences:
    sentences.append(sentence.string)
  return { "sentences": sentences }

@router.get("/status")
async def getStatus():
  return
