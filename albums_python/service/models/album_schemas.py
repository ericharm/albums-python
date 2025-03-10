from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from marshmallow_dataclass import class_schema

from albums_python.domain.utils import char_field_to_str, int_field_to_int
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
        return AlbumResponse(
            id=int_field_to_int(album.id),
            artist=char_field_to_str(album.artist),
            released=char_field_to_str(album.released),
            title=f"{album.title}",
            format=char_field_to_str(album.format),
            label=char_field_to_str(album.label),
            created_at=album.created_at,
            updated_at=album.updated_at,
            notes=char_field_to_str(album.notes),
            genres=[genre.name for genre in album.genres],
        )


AlbumResponseSchema = class_schema(AlbumResponse)()


@dataclass
class AlbumsIndexResponse(PaginatedResponse):
    albums: list[AlbumResponse]


AlbumsIndexResponseSchema = class_schema(AlbumsIndexResponse)()
