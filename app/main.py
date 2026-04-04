from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1.reports import router as reports_router
from app.core.config import settings
from app.core.database import check_db_connection


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

app.include_router(reports_router, prefix="/api/v1")


@app.get("/health", tags=["health"])
async def health_check() -> dict:
    db_ok = await check_db_connection()
    return {"status": "ok", "db": "connected" if db_ok else "unreachable"}
