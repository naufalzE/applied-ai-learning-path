from app.schemas.translate_schema import TranslateRequest
from app.core.logger import logger


class TranslateService:

    def translate(self,request:TranslateRequest):
        logger.warning("Translate dimulai")
        return {
            "translated_text": f"[{request.target_language}] {request.text}"
}