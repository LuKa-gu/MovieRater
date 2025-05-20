from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from . import models, database
from .models import Movie
from datetime import date, datetime

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request, db: Session = Depends(get_db)):
    movies = db.query(Movie).all()

    # Pretvorba datuma v slovenski format
    for movie in movies:
        if movie.date:
            try:
                movie.date_display = movie.date.strftime("%d. %m. %Y")
            except ValueError:
                movie.date_display = movie.date  # fallback, če je napačen format
        else:
            movie.date_display = "Ni datuma"

    return templates.TemplateResponse("index.html", {"request": request, "movies": movies})

@app.post("/movies")
def create_movie(
    title: str = Form(...),
    genre: str = Form(...),
    rating: float = Form(...),
    date: date = Form(...),
    db: Session = Depends(get_db)
):
    movie = Movie(title=title, genre=genre, rating=rating, date=date)
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return RedirectResponse(url="/", status_code=303)

@app.post("/movies/{movie_id}/delete")
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if movie:
        db.delete(movie)
        db.commit()
    return RedirectResponse(url="/", status_code=303)

@app.post("/movies/{movie_id}/update")
def update_movie(
    movie_id: int,
    title: str = Form(...),
    genre: str = Form(...),
    rating: float = Form(...),
    date: date = Form(...),
    db: Session = Depends(get_db)
):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if movie:
        movie.title = title
        movie.genre = genre
        movie.rating = rating
        movie.date = date
        db.commit()
    return RedirectResponse(url="/", status_code=303)
