from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    country = Column(String, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    