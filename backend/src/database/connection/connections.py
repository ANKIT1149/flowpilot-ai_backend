from sqlalchemy.ext.asyncio import create_async_engine
from backend.src.core.config import settings

DATABASE_URL = settings.DATABASE_URL.replace(
    "postgresql://", 
    "postgresql+asyncpg://"
)

engine = create_async_engine(
    DATABASE_URL,
    echo=settings.ENVIRONMENT == "development",
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20,
)
