from peewee import ForeignKeyField, IntegerField

from albums_python.query.models.album import Album
from albums_python.query.models.genre import Genre
from albums_python.query.models.model import Model


class AlbumGenre(Model):
    class Meta:
        table_name = "album_genres"

    id = IntegerField(primary_key=True)
    album = ForeignKeyField(Album, backref="album_genres")
    genre = ForeignKeyField(Genre, backref="genre_albums")
