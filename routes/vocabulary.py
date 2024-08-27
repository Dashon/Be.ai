from fastapi import APIRouter, Depends
from models.vocabulary import VocabularyItem
from services.vocabulary_service import add_vocabulary

router = APIRouter()


@router.post("/")
def add_vocab(item: VocabularyItem):
    result = add_vocabulary(item)
    return {"result": result}
