from sqlalchemy import Column, Integer, String, ForeignKey, JSON, Float
from sqlalchemy.orm import relationship
from app.database import Base

class Accommodation(Base):
    __tablename__ = 'accommodations'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    rating = Column(Float, nullable=True)
    number_of_reviews = Column(Integer, nullable=True)
    amenities = Column(JSON, nullable=True)

    source = Column(String, nullable=True)
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=True)
    city = relationship("City", backref="accommodations")