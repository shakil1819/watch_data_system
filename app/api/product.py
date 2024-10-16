from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from app.services.product_service import ProductService
from app.schemas.product import ProductResponse, ProductCreate, ProductUpdate
from app.schemas.review import ReviewResponse

router = APIRouter()

@router.get("/", response_model=List[ProductResponse])
async def list_products(
    search: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    min_rating: Optional[float] = None,
    sort_by: Optional[str] = None,
    sort_order: Optional[str] = "asc",
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100)
):
    """
    List products with search, filter, sort, and pagination functionalities.
    """
    return await ProductService.list_products(
        search, min_price, max_price, min_rating, sort_by, sort_order, page, limit
    )

@router.get("/top", response_model=List[ProductResponse])
async def get_top_products(
    limit: int = Query(10, ge=1, le=50)
):
    """
    Get top products based on average rating and number of reviews.
    """
    return await ProductService.get_top_products(limit)

@router.get("/{product_id}/reviews", response_model=List[ReviewResponse])
async def get_product_reviews(
    product_id: int,
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100)
):
    """
    Get reviews for a specific product with pagination.
    """
    return await ProductService.get_product_reviews(product_id, page, limit)

@router.post("/", response_model=ProductResponse)
async def create_product(product: ProductCreate):
    return await ProductService.create_product(product)

@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(product_id: int, product: ProductUpdate):
    return await ProductService.update_product(product_id, product)

@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(product_id: int):
    return await ProductService.get_product(product_id)
