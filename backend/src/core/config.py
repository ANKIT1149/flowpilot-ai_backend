from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration loaded from the .env file.

    This class is the single source of truth for all environment variables.
    """

    APP_NAME: str = Field(default="CreatorLens AI")
    APP_VERSION: str = Field(default="1.0.0")
    ENVIRONMENT: str = Field(default="development")
    DEBUG: bool = Field(default=True)
    CACHE_TTL: int = Field(default=3600, description="Cache time-to-live in seconds")
    DATABASE_URL: str = ''
    REDIS_URL: str = ''
    RABBITMQ_URL: str= ''
    CORS_ORIGINS: str = ''
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

@lru_cache()
def get_settings() -> "Settings":
    """
        Get the application settings.

        This function uses caching to ensure that the settings are only loaded once.
        """
    return Settings()

settings = get_settings()
