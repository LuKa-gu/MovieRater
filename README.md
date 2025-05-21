# MovieRater 🎬

**MovieRater** je preprosta spletna aplikacija za ocenjevanje filmov, izdelana s pomočjo **FastAPI**, **SQLAlchemy** in **Jinja2**. Podatki se shranjujejo v SQLite podatkovno bazo. Aplikacija omogoča dodajanje, urejanje in brisanje filmov, kakor tudi prikaz vseh filmov v prijaznem spletnem vmesniku.

## Značilnosti

* ✏️ Dodaj film z naslovom, žanrom, oceno (1–10) in datumom ogleda.
* 📋 Preglej vse dodane filme.
* 🛠️ Uredi film na seznamu.
* ❌ Izbriši film iz seznama.

## Zahteve

* Docker in Docker Compose

## Zagon projekta z Dockerjem

1. **Prvi zagon (ali ko spremeniš kodo)**:

   ```bash
   sudo docker compose up --build
   ```

2. **Običajen zagon brez sprememb**:

   ```bash
   sudo docker compose up
   ```

3. **Zaustavitev aplikacije**:

   ```bash
   sudo docker compose down
   ```

## Struktura projekta

```
movierater/
├── app/
│   ├── database.py
│   ├── main.py
│   ├── models.py
├── templates/
│   └── index.html
├── Dockerfile
├── movies.db
├── requirements.txt
├── README.md
└── docker-compose.yml
```

## API dokumentacija

FastAPI samodejno generira interaktivno dokumentacijo:

* Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
* ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Endpoints

#### GET `/`

Prikaže glavno stran z obrazcem in seznamom filmov.

#### POST `/movies`

Dodaj nov film.

**Body (form):**

* `title`: naslov (str)
* `genre`: žanr (str)
* `rating`: ocena (float, 1–10)
* `date`: datum (YYYY-MM-DD)

#### POST `/movies/{movie_id}/delete`

Izbriši film z določenim ID-jem.

#### POST `/movies/{movie_id}/update`

Posodobi obstoječ film.

**Body (form):**

* `title`: nov naslov
* `genre`: nov žanr
* `rating`: nova ocena
* `date`: nov datum

---