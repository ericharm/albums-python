from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from marshmallow_dataclass import class_schema

from albums_python.query.models.album import Album
from albums_python.service.models.http import PaginatedResponse


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

    @staticmethod
    def from_album(album: Album) -> AlbumResponse:
        return AlbumResponse(
            id=album.id,
            artist=album.artist,
            released=album.released,
            title=album.title,
            format=album.format,
            label=album.label,
            created_at=album.created_at,
            updated_at=album.updated_at,
            notes=album.notes,
        )


AlbumResponseSchema = class_schema(AlbumResponse)()


@dataclass
class AlbumsIndexResponse(PaginatedResponse):
    albums: list[AlbumResponse]


AlbumsIndexResponseSchema = class_schema(AlbumsIndexResponse)()
