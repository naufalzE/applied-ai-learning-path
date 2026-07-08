from fastapi import APIRouter, Depends

from app.schemas.summarize_schema import SummarizeRequest
from app.services.summarize_service import SummarizeService

from app.dependencies.summarize_dependencies import (
    get_summarize_service
)

router = APIRouter(
    prefix="/summarize",
    tags=["Summarize"]
)


@router.post("/")
def post_summarize( request: SummarizeRequest,service: SummarizeService = Depends( get_summarize_service)):

    result = service.generate_summary(request.text)

    return {
        "summary": result
    }


@router.get("/health")
def get_health():

    return {
        "status": "OK"
    }