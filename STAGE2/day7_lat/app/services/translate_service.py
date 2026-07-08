from app.schemas.translate_schema import TranslateRequest

class TranslateService:

    def translate(self,request:TranslateRequest):

        return {
            "translated_text": f"[{request.target_language}] {request.text}"
}