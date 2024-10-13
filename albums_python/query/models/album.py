from datetime import datetime
from typing import Optional

from peewee import CharField, DateTimeField, IntegerField

from albums_python.domain.utils import current_utc_datetime
from albums_python.query.models.model import Model


class Album(Model):
    class Meta:
        table_name = "albums"

    id: int = IntegerField(primary_key=True)
    artist: Optional[str] = CharField(null=True)
    released: Optional[str] = CharField(null=True)
    title: str = CharField(null=False)
    format: Optional[str] = CharField(null=True)  # TODO convert to Enum
    label: Optional[str] = CharField(null=True)
    notes: Optional[str] = CharField(null=True)
    created_at: datetime = DateTimeField(default=current_utc_datetime)
    updated_at: datetime = DateTimeField(default=current_utc_datetime)

    def __repr__(self) -> str:
        return f"Album<id={self.id}, artist={self.artist}, title={self.title}>"

    @property
    def genres(self) -> list["AlbumGenre"]:
        return [album_genre.genre for album_genre in self.album_genres]
