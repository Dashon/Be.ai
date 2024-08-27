from fastapi import APIRouter, Depends
from app.models.translation import TranslationRequest
from app.services.translation_service import translate_text

router = APIRouter()

@router.post("/")
def translate(request: TranslationRequest):
    translated_text = translate_text(request)
    return {"translated_text": translated_text}
