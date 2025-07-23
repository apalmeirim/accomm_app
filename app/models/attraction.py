from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Attraction(Base):
    __tablename__ = 'attractions'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    popularity = Column(Float, nullable=True)

    city_id = Column(Integer, ForeignKey('cities.id'), nullable=True)
    city = relationship("City", backref="attractions")

    