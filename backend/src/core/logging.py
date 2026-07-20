import sys
from loguru import logger
from backend.src.core.config import settings

logger.remove();

logger.add(
    sys.stdout,
    level="DEBUG" if settings.ENVIRONMENT == "development" else "INFO",
    format=(
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level:<8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
        "<level>{message}</level>"
    ),
    colorize=True,
)

logger.add(
    "logs/application.log",
    rotation="10 MB",
    retention="10 days",
    compression="zip",
    level="INFO",
)


