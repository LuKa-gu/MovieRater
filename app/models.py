from sqlalchemy import Column, Integer, String, Float, Date
from pydantic import BaseModel, Field
from datetime import date
from .database import Base

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    genre = Column(String)
    rating = Column(Float)
    date = Column(Date)

# Pydantic sheme
class MovieCreate(BaseModel):
    title: str
    genre: str
    rating: float = Field(..., ge=0, le=10)
    date: date

class MovieOut(BaseModel):
    id: int
    title: str
    genre: str
    rating: float
    date: date

    class Config:
        from_attributes = True
