from fastapi import FastAPI

from app.core.config import settings
from app.routers.summarize import router as summarize_router


app = FastAPI(
    title=settings.app_name
)


app.include_router(summarize_router)