from fastapi import APIRouter

from app.schemas.summarize_schema import SummarizeRequest
from app.services.summarize_service import SummarizeService


router = APIRouter()

service = SummarizeService()


@router.post("/summarize")
def post_summarize(request: SummarizeRequest):

    result = service.generate_summary(
        request.text
    )

    return {
        "summary": result
    }


@router.get("/health")
def get_health():

    return {
        "status": "OK"
    }