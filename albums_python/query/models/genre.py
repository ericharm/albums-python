from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from albums_python.query.models.album_genre import album_genres_table
from albums_python.query.models.model import Model


class Genre(Model):
    __tablename__ = "genres"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    albums: Mapped[list["Album"]] = relationship(  # type: ignore
        "Album", secondary=album_genres_table, back_populates="genres"
    )

    def __repr__(self) -> str:
        return f"Genre<id={self.id}, name={self.name}>"
