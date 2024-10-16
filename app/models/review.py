from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.db import Base

# Add this check to prevent redefining the table
if 'reviews' not in Base.metadata.tables:
    class Review(Base):
        __tablename__ = 'reviews'

        id = Column(Integer, primary_key=True, index=True)
        text = Column(String)
        rating = Column(Integer)
        product_id = Column(Integer, ForeignKey('products.id'))
        product = relationship("Product")
else:
    # If the table is already defined, just get the existing table
    Review = Base.metadata.tables['reviews']
