from fastapi import FastAPI

from app.core.config import settings
from app.routers.translate import router as translate_router
from app.core.logger import logger

logger.info("Server Berjalan")
app = FastAPI(
    title=settings.app_name
)

app.include_router(translate_router)