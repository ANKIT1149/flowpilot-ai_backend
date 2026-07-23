from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from backend.src.core.config import settings
from backend.src.core.logging import logger
from backend.src.api.health import health 
from backend.src.database.repositories.session import get_db 
from backend.src.api.health import test
from fastapi.middleware.cors import CORSMiddleware
from backend.src.api.routes.service.urlvalidating import router  as url_validation_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        settings.CORS_ORIGINS
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    logger.success(f"{settings.APP_NAME} started successfully.")


@app.get("/")
def read_root():
    return {"message": f"Welcome to {settings.APP_NAME}"}


@app.get("/db")
async def get_database_request(db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT 1"))
    return {"message": "Database connected successfully!"}


@app.get("/health")
async def health_endpoint(db: AsyncSession = Depends(get_db)):
    return await health(db=db)

@app.get("/redis/test")
async def test_redis():
    return await test()

@app.get("/ping")
def ping():
    logger.info("Ping request received.")
    return {"message": "pong"}

app.include_router(url_validation_router)
