from pydantic import BaseModel

class VocabularyItem(BaseModel):
    term: str
    definition: str
    context: str
