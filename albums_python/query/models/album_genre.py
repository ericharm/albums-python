from peewee import ForeignKeyField

from albums_python.query.models.album import Album
from albums_python.query.models.genre import Genre
from albums_python.query.models.model import Model


class AlbumGenre(Model):
    class Meta:
        table_name = "album_genres"

    album: int = ForeignKeyField(Album, backref="album_genres")
    genre: int = ForeignKeyField(Genre, backref="genre_albums")
