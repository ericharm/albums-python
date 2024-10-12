from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from albums_python.query.models.model import Model


class AlbumGenre(Model):
    __tablename__ = "album_genres"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    album_id: Mapped[int] = mapped_column(Integer, ForeignKey("albums.id"), nullable=False)
    genre_id: Mapped[int] = mapped_column(Integer, ForeignKey("genres.id"), nullable=False)
