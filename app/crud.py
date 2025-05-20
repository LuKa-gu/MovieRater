from sqlalchemy.orm import Session
from .models import Movie

def get_movies(db: Session):
    return db.query(Movie).all()

def create_movie(db: Session, title: str, genre: str, rating: int):
    movie = Movie(title=title, genre=genre, rating=rating)
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie

def delete_movie(db: Session, movie_id: int):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if movie:
        db.delete(movie)
        db.commit()
