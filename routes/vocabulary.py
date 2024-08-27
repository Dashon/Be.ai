from fastapi import APIRouter, Depends
from app.models.vocabulary import VocabularyItem
from app.services.vocabulary_service import add_vocabulary

router = APIRouter()

@router.post("/")
def add_vocab(item: VocabularyItem):
    result = add_vocabulary(item)
    return {"result": result}
