from __future__ import annotations

from dataclasses import dataclass

from marshmallow_dataclass import class_schema

from albums_python.domain.utils import int_field_to_int
from albums_python.query.models.album_genre import AlbumGenre
from albums_python.query.models.genre import Genre


@dataclass()
class AlbumGenreResponse:
    id: int
    album_id: int
    genre_id: int
    genre_name: str

    @staticmethod
    def from_album_genre(album_genre: AlbumGenre, genre: Genre) -> AlbumGenreResponse:
        return AlbumGenreResponse(
            id=int_field_to_int(album_genre.id),
            album_id=int_field_to_int(album_genre.album.id),
            genre_id=int_field_to_int(album_genre.genre.id),
            genre_name=f"{genre.name}",
        )


AlbumGenreResponseSchema = class_schema(AlbumGenreResponse)()
