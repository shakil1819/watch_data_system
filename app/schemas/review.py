from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ReviewBase(BaseModel):
    product_id: int
    rating: int
    comment: str

class ReviewCreate(ReviewBase):
    pass

class ReviewUpdate(ReviewBase):
    product_id: Optional[int] = None
    rating: Optional[int] = None
    comment: Optional[str] = None

class ReviewResponse(ReviewBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
