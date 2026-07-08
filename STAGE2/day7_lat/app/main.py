from fastapi import FastAPI

from app.core.config import settings
from app.routers.translate import router as translate_router

app = FastAPI(
    title=settings.app_name
)

app.include_router(translate_router)