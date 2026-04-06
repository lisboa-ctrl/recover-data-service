from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.controllers import health_router, report_router
from app.infrastructure.config import settings
from app.infrastructure.database import check_db_connection


@asynccontextmanager
async def lifespan(app: FastAPI):
    connected = await check_db_connection()
    if not connected:
        raise RuntimeError("Could not connect to the database on startup")
    yield


app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(health_router)
app.include_router(report_router, prefix="/api/v1")
