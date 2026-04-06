from fastapi import APIRouter

from app.infrastructure.database import check_db_connection

router = APIRouter(tags=["health"])


@router.get("/health")
async def health_check() -> dict:
    db_ok = await check_db_connection()
    return {"status": "ok", "db": "connected" if db_ok else "unreachable"}
