import asyncio
import base64
import json

import requests

from grooverspotify import models
from grooverspotify.database import SessionLocal, engine
from grooverspotify.models import Artist
from grooverspotify.spotify import fetch_latest_releases

def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()

db = get_db()

models.ModelBase.metadata.create_all(bind=engine)

def insert_artist(raw_data):
    data = raw_data.copy()
    data["external_urls"] = json.dumps(data["external_urls"])
    data["spotify_key"] = data["id"]
    del data["id"]
    artist = Artist(**data)
    db.add(artist)
    db.commit()
    db.refresh(artist)


async def fetch_releases() -> int:
    releases = fetch_latest_releases()

    artists_count = 0
    try:
        albums = releases["albums"]["items"]
    except KeyError:
        return artists_count

    for album in albums:
        for artist in album["artists"]:
            try:
                insert_artist(artist)
                artists_count += 1
            except Exception as e:
                print(e)
                pass

    return artists_count


async def main():
    try:
        artists_count = await fetch_releases()
        print("No new artists for now" if not artists_count else f"Found {artists_count} new artist(s)")
    except Exception as e:
        print("Looks like something went wrong on our side...", e)

if __name__ == "__main__":
    asyncio.run(main())