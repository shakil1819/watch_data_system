from fastapi import FastAPI
from app.api import product, review, insight
from app.core.database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(product.router, prefix="/api/products", tags=["Product"])
app.include_router(review.router, prefix="/api/reviews", tags=["Review"])
app.include_router(insight.router, prefix="/api/insights", tags=["Insight"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Watch Data System API"}
