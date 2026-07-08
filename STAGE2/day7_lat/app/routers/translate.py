from fastapi import APIRouter, Depends
from app.schemas.translate_schema import TranslateRequest
from app.services.translate_service import TranslateService
from app.dependencies.translate_dependencies import (get_translate_service)

router = APIRouter(
    prefix="/translate",
    tags=["Translate"]
)

@router.post("/")
def post_translate(request:TranslateRequest,service:TranslateService = Depends(get_translate_service)):
    
    return service.translate(request)

    