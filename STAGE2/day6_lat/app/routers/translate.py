from fastapi import APIRouter, Depends
from app.schemas.translate_schema import TranslateRequest
from app.services.translate_service import TranslateService
from app.dependencies.translate_dependencies import (get_translate_service)
from app.core.logger import logger


router = APIRouter(
    prefix="/translate",
    tags=["Translate"]
)

@router.post("/")
def post_translate(request:TranslateRequest,service:TranslateService = Depends(get_translate_service)):
    logger.info("Request Masuk")
    return service.translate(request)

    