from fastapi import APIRouter, HTTPException
from app.services.product_service import ProductService
from app.schemas.product import ProductCreate, ProductUpdate

router = APIRouter()

@router.get("/")
async def list_products():
    return ProductService.list_products()

@router.post("/")
async def create_product(product: ProductCreate):
    return ProductService.create_product(product)

@router.put("/{product_id}")
async def update_product(product_id: int, product: ProductUpdate):
    return ProductService.update_product(product_id, product)

@router.get("/{product_id}")
async def get_product(product_id: int):
    return ProductService.get_product(product_id)