from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional, cast

from marshmallow_dataclass import class_schema
from peewee import CharField, IntegerField

from albums_python.query.models.album import Album
from albums_python.service.models.http import PaginatedRequest, PaginatedResponse


@dataclass
class SearchAlbumsRequest(PaginatedRequest):
    query: Optional[str] = None


SearchAlbumsRequestSchema = class_schema(SearchAlbumsRequest)()


@dataclass
class AlbumRequest:
    artist: Optional[str]
    released: Optional[str]
    title: str
    format: Optional[str]
    label: Optional[str]
    notes: Optional[str]


AlbumRequestSchema = class_schema(AlbumRequest)()


@dataclass
class AlbumResponse:
    id: int
    artist: Optional[str]
    released: Optional[str]
    title: str
    format: Optional[str]
    label: Optional[str]
    created_at: datetime
    updated_at: datetime
    notes: Optional[str]
    genres: list[str]

    @staticmethod
    def from_album(album: Album) -> AlbumResponse:
        return AlbumResponse(  # type: ignore
            id=_int_field_to_int(album.id),
            artist=_char_field_to_str(album.artist),
            released=_char_field_to_str(album.released),
            title=f"{album.title}",
            format=_char_field_to_str(album.format),
            label=_char_field_to_str(album.label),
            created_at=album.created_at,
            updated_at=album.updated_at,
            notes=_char_field_to_str(album.notes),
            genres=[genre.name for genre in album.genres],
        )


AlbumResponseSchema = class_schema(AlbumResponse)()


@dataclass
class AlbumsIndexResponse(PaginatedResponse):
    albums: list[AlbumResponse]


AlbumsIndexResponseSchema = class_schema(AlbumsIndexResponse)()


def _int_field_to_int(value: IntegerField) -> int:
    return cast(int, value)


def _char_field_to_str(value: CharField) -> Optional[str]:
    if value is None:
        return None
    return f"{value}"
