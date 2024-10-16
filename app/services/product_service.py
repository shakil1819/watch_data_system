from sqlalchemy import func, desc
from sqlalchemy.orm import joinedload
from app.core.db import get_db
from app.models.product import Product
from app.models.review import Review
from app.schemas.product import ProductCreate, ProductUpdate
from fastapi import HTTPException

class ProductService:

    @staticmethod
    async def list_products(search, min_price, max_price, min_rating, sort_by, sort_order, page, limit):
        db = next(get_db())
        query = db.query(Product)

        if search:
            query = query.filter(Product.name.ilike(f"%{search}%") | Product.brand.ilike(f"%{search}%"))
        if min_price:
            query = query.filter(Product.price >= min_price)
        if max_price:
            query = query.filter(Product.price <= max_price)
        if min_rating:
            query = query.filter(Product.average_rating >= min_rating)

        if sort_by:
            order = desc if sort_order == "desc" else asc
            query = query.order_by(order(getattr(Product, sort_by)))

        total = query.count()
        products = query.offset((page - 1) * limit).limit(limit).all()

        return {"total": total, "items": products}

    @staticmethod
    async def get_top_products(limit):
        db = next(get_db())
        top_products = db.query(Product).order_by(
            desc(Product.average_rating),
            desc(Product.review_count)
        ).limit(limit).all()

        return top_products

    @staticmethod
    async def get_product_reviews(product_id, page, limit):
        db = next(get_db())
        product = db.query(Product).filter(Product.id == product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        reviews = db.query(Review).filter(Review.product_id == product_id).offset((page - 1) * limit).limit(limit).all()
        return reviews

    @staticmethod
    async def create_product(product: ProductCreate):
        db = next(get_db())
        db_product = Product(**product.dict())
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product

    @staticmethod
    async def update_product(product_id: int, product: ProductUpdate):
        db = next(get_db())
        db_product = db.query(Product).filter(Product.id == product_id).first()
        if not db_product:
            raise HTTPException(status_code=404, detail="Product not found")
        for key, value in product.dict(exclude_unset=True).items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
        return db_product

    @staticmethod
    async def get_product(product_id: int):
        db = next(get_db())
        product = db.query(Product).filter(Product.id == product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product
