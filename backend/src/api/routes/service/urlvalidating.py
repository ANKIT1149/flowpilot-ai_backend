from fastapi import APIRouter
from backend.src.services.URLValidateService import validate_url
from backend.src.model.URLValidateModel import VideoRequest
from backend.src.core.logging import logger

router = APIRouter()

@router.post("/url_validate")
async def url_validate(request: VideoRequest):
    result = await validate_url(str(request.url))
    return result

