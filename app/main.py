from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from . import models, database, crud

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
    movies = crud.get_movies(db)
    return templates.TemplateResponse("index.html", {"request": request, "movies": movies})

@app.post("/add")
def add_movie(title: str, genre: str, rating: int, db: Session = Depends(get_db)):
    return crud.create_movie(db, title, genre, rating)

@app.delete("/delete/{movie_id}")
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    crud.delete_movie(db, movie_id)
    return {"message": "Deleted"}
