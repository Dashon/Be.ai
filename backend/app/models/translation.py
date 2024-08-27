from pydantic import BaseModel


class TranslationRequest(BaseModel):
    regional_variation: str
    generational_influence: int
    socio_economic_context: str
    cultural_influences: list
    code_switching: bool
    geographical_setting: str
    text: str
    source_lang: str
    target_lang: str
