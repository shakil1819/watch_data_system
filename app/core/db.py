from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

DATABASE_URL = "postgresql://root:root@172.18.0.3:5432/watchdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Watch(Base):
    __tablename__ = "watches"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String)
    model = Column(String)
    price = Column(Float)
    material = Column(String)
    water_resistance = Column(String)
    image_url = Column(String)
    category = Column(String)
    asin = Column(String, unique=True)
    reviews = relationship("Review", back_populates="watch")

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    watch_id = Column(Integer, ForeignKey("watches.id"))
    rating = Column(Float)
    review_text = Column(String)
    reviewer_name = Column(String)
    review_date = Column(DateTime)
    watch = relationship("Watch", back_populates="reviews")

Base.metadata.create_all(bind=engine)

