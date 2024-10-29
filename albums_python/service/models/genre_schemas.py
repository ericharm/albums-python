from __future__ import annotations

from dataclasses import dataclass

from marshmallow_dataclass import class_schema

from albums_python.domain.utils import int_field_to_int
from albums_python.query.models.genre import Genre


@dataclass
class CreateGenreRequest:
    name: str


CreateGenreRequestSchema = class_schema(CreateGenreRequest)()


@dataclass
class GenreResponse:
    id: int
    name: str

    @staticmethod
    def from_genre(genre: Genre) -> GenreResponse:
        return GenreResponse(
            id=int_field_to_int(genre.id),
            name=f"{genre.name}",
        )


GenreResponseSchema = class_schema(GenreResponse)()
