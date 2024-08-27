from fastapi import APIRouter, Depends
from models.translation import TranslationRequest
from services.translation_service import translate_text

router = APIRouter()


@router.post("/")
def translate(request: TranslationRequest):
    translated_text = translate_text(request)
    return {"translated_text": translated_text}
