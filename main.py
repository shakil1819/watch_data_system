from fastapi import FastAPI
from app.api import product, review, insight
from app.core.db import Base, engine
from scheduler import schedule_scraper
import threading
import uvicorn

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(product.router, prefix="/api/products", tags=["Product"])
app.include_router(review.router, prefix="/api/reviews", tags=["Review"])
app.include_router(insight.router, prefix="/api/insights", tags=["Insight"])

# Start the scheduler in a separate thread
scheduler_thread = threading.Thread(target=schedule_scraper)
scheduler_thread.start()

@app.get("/")
def root():
    return {"message": "Welcome to the Watch Data System API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
