from fastapi import APIRouter, HTTPException
from app.services.review_service import ReviewService
from app.schemas.review import ReviewCreate, ReviewUpdate

router = APIRouter()

@router.get("/")
async def list_reviews():
    return ReviewService.list_reviews()

@router.post("/")
async def create_review(review: ReviewCreate):
    return ReviewService.create_review(review)

@router.put("/{review_id}")
async def update_review(review_id: int, review: ReviewUpdate):
    return ReviewService.update_review(review_id, review)

@router.get("/{review_id}")
async def get_review(review_id: int):
    return ReviewService.get_review(review_id)