from datetime import datetime
from typing import Any

from peewee import CharField, DateTimeField, IntegerField

from albums_python.domain.utils import current_utc_datetime
from albums_python.query.models.model import Model


class Album(Model):
    class Meta:
        table_name = "albums"

    id = IntegerField(primary_key=True)
    artist = CharField(null=True)
    released = CharField(null=True)
    title = CharField(null=False)
    format = CharField(null=True)
    label = CharField(null=True)
    notes = CharField(null=True)
    created_at: datetime = DateTimeField(default=current_utc_datetime)  # type: ignore
    updated_at: datetime = DateTimeField(default=current_utc_datetime)  # type: ignore

    def __repr__(self) -> str:
        return f"Album<id={self.id}, artist={self.artist}, title={self.title}>"

    def save(self, *args: Any, **kwargs: Any) -> None:
        self.updated_at = current_utc_datetime()
        super().save(*args, **kwargs)

    @property
    def genres(self) -> list["AlbumGenre"]:  # type: ignore # noqa: F821
        return [album_genre.genre for album_genre in self.album_genres]  # type: ignore
