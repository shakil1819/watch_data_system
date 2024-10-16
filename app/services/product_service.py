from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate
from app.core.database import SessionLocal

class ProductService:

    @staticmethod
    def list_products():
        with SessionLocal() as session:
            return session.query(Product).all()

    @staticmethod
    def create_product(product: ProductCreate):
        with SessionLocal() as session:
            new_product = Product(**product.dict())
            session.add(new_product)
            session.commit()
            session.refresh(new_product)
            return new_product

    @staticmethod
    def update_product(product_id: int, product: ProductUpdate):
        with SessionLocal() as session:
            db_product = session.query(Product).filter(Product.id == product_id).first()
            if not db_product:
                raise HTTPException(status_code=404, detail="Product not found")
            for field, value in product.dict().items():
                setattr(db_product, field, value)
            session.commit()
            session.refresh(db_product)
            return db_product

    @staticmethod
    def get_product(product_id: int):
        with SessionLocal() as session:
            return session.query(Product).filter(Product.id == product_id).first()