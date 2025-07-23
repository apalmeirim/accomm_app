from sqlalchemy import Column, Integer, ForeignKey, Float, JSON, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class UserSearch(Base):
    __tablename__ = 'user_searches'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=True)

    selected_attraction_ids = Column(JSON, nullable=True)
    budget_min = Column(Float, nullable=True)
    budget_max = Column(Float, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", backref="searches")
    city = relationship("City", backref="searches")
    