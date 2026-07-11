from pydantic import BaseModel,Field
from enum import Enum

class Language(str, Enum):
    EN = "en"
    ID = "id"
    ES = "es"
    FR = "fr"
    JA = "ja"
    
class TranslateRequest(BaseModel):
    text: str = Field(
        min_length=2,
        description="Text to translate",
        max_length=2000
        )
    target_language: Language
    
    
    
class TranslateResponse(BaseModel):
    translated_text: str
    source_language: Language
    target_language: Language

