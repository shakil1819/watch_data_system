from pydantic import BaseModel
from typing import Optional, List
from app.schemas.review import ReviewResponse

class ProductBase(BaseModel):
    name: str
    brand: str
    price: float
    description: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    name: Optional[str] = None
    brand: Optional[str] = None
    price: Optional[float] = None

class ProductResponse(ProductBase):
    id: int
    average_rating: float
    review_count: int
    reviews: Optional[List[ReviewResponse]] = None

    class Config:
        orm_mode = True

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
