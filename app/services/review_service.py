from app.models.review import Review
from app.schemas.review import ReviewCreate, ReviewUpdate
from app.core.database import SessionLocal

class ReviewService:

    @staticmethod
    def list_reviews():
        with SessionLocal() as session:
            return session.query(Review).all()

    @staticmethod
    def create_review(review: ReviewCreate):
        with SessionLocal() as session:
            new_review = Review(**review.dict())
            session.add(new_review)
            session.commit()
            session.refresh(new_review)
            return new_review

    @staticmethod
    def update_review(review_id: int, review: ReviewUpdate):
        with SessionLocal() as session:
            db_review = session.query(Review).filter(Review.id == review_id).first()
            if not db_review:
                raise HTTPException(status_code=404, detail="Review not found")
            for field, value in review.dict().items():
                setattr(db_review, field, value)
            session.commit()
            session.refresh(db_review)
            return db_review

    @staticmethod
    def get_review(review_id: int):
        with SessionLocal() as session:
            return session.query(Review).filter(Review.id == review_id).first()