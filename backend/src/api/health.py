from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from backend.src.cache.cache_service import cache_service
from backend.src.database.repositories.session import get_db

router = APIRouter()


@router.get("/health")
async def health(
    db: AsyncSession = Depends(get_db),
):
    await db.execute(text("SELECT 1"))

    return {
        "status": "healthy",
        "database": "connected",
    }


@router.get("/redis/test")
async def test():

    await cache_service.set(
        "hello",
        "world",
        60,
    )

    value = await cache_service.get("hello")

    return {"redis": value}
