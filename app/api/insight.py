from fastapi import APIRouter
from app.services.insight_service import InsightService

router = APIRouter()

@router.get("/")
async def get_insights():
    return InsightService.get_insights()