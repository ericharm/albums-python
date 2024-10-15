from peewee import CharField, IntegerField

from albums_python.query.models.model import Model


class Genre(Model):
    class Meta:
        table_name = "genres"

    id: int = IntegerField(primary_key=True)
    name: str = CharField(null=False)

    def __repr__(self) -> str:
        return f"Genre<id={self.id}, name={self.name}>"

    @property
    def albums(self) -> list["AlbumGenre"]:  # noqa: F821
        return [album_genre.album for album_genre in self.genre_albums]
