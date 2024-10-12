from sqlalchemy import Column, ForeignKey, Integer, Table

from albums_python.query.models.model import Model

album_genres_table = Table(
    "album_genres",
    Model.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("album_id", Integer, ForeignKey("albums.id"), nullable=False),
    Column("genre_id", Integer, ForeignKey("genres.id"), nullable=False),
)
