from pydantic import BaseModel

class PartOfSpeech(BaseModel):
  tag: str
