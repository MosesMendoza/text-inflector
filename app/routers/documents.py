from fastapi import APIRouter

router = APIRouter()

@router.get("/documents", tags=["users"])
async def read_documents():
  return [{"document": "foo"}]
