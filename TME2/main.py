from typing import Optional
from fastapi import FastAPI, Query
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()
app.mount("/images", StaticFiles(directory="back-end/images"), name="Image")
DATA_PATH = Path(__file__).parent / "movies.json"

# Configuration du CORS, pour permettre les requêtes depuis le front-end, ici localhost:5173
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173","http://127.0.0.1:5173"],            # Autorise les sites dans la liste
    allow_credentials=True,
    allow_methods=["*"],              # Autorise tous les types de requêtes (GET, POST, etc.)
    allow_headers=["*"],              # Autorise tous les headers
)

@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}

#ici avec ou sans paramètre, optionnel, grâce à Optional, et on gère les deux cas dans la fonction
def get_movies(limit: Optional[int] = Query(None, gt=0)):
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        movies = json.load(f)
    if limit is not None:
        return movies[:limit]
    return movies

#longeur est optionnel, s'il est fourni, on retourne seulement les premiers 'limit' films, sinon on retourne tous les films
@app.get("/movies")
def movies_query(limit: Optional[int] = Query(None, gt=0)):
    return get_movies(limit)

#longeur est obligatoire, on retourne seulement les premiers 'limit' films
@app.get("/movies/{limit}")
def movies_path(limit: int):
    return get_movies(limit)