from pydantic import BaseModel

class ReviewBase(BaseModel):
    text: str
    rating: int

class ReviewCreate(ReviewBase):
    pass

class ReviewUpdate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    product_id: int

    class Config:
        orm_mode = True