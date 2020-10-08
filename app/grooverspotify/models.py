from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from grooverspotify.database import ModelBase


class Artist(ModelBase):
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True, index=True)
    external_urls = Column(String)
    href = Column(String)
    name = Column(String)
    type = Column(String)
    uri = Column(String)
    spotify_key = Column(String)
    # album_id = Column(Integer, ForeignKey(Album.id))


# Just keeping those classes as a reminder
# class Album(ModelBase):
#     __tablename__ = "albums"

#     id = Column(Integer, primary_key=True, index=True)
#     album_type = Column(String, unique=True, index=True)
#     available_markets = Column(String)
#     external_urls = Column(String)
#     href = Column(String)
#     images = Column(String)
#     name = Column(String)
#     type = Column(String)
#     uri = Column(String)
#     spotify_key = Column(String)

#     images = relationship("Image", backref="album")
#     artists = relationship("Artist", backref="album")


# class Image(ModelBase):
#     __tablename__ = "images"

#     id = Column(Integer, primary_key=True, index=True)
#     url = Column(String)
#     height = Column(Integer)
#     width = Column(Integer)
#     album_id = Column(Integer, ForeignKey(Album.id))
