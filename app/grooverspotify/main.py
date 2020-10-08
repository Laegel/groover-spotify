from datetime import datetime
import json
from typing import List, Optional

from fastapi import Depends, FastAPI, Request, Response
from pydantic import BaseModel
from sqlalchemy.orm import Session

from grooverspotify import models
from grooverspotify.database import SessionLocal

app = FastAPI()

def get_db(request: Request):
    return request.state.db


class Artist(BaseModel):
    id: str
    external_urls: str
    href: str
    name: str
    type: str
    uri: str
    spotify_key: str


ArtistsOutputPayload = List[Artist]


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


@app.get("/")
def read_root():
    return {"message": "Welcome! You may find artists who have recently released music at '/api/artists/'"}

#, response_model=ArtistsOutputPayload
@app.get("/api/artists/")
async def get_artists(db: Session = Depends(get_db)):
    """Get artists who have recently released an album. 
    No HTTP errors are to be expected in a REST webservice for this kind of route, even if there is no data."""
    artists = db.query(models.Artist).all()
    return artists
