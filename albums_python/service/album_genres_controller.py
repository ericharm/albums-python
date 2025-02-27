from typing import Union

from flask import Blueprint

from albums_python.domain import albums as albums_domain
from albums_python.domain.album_genres import is_album_already_associated_with_genre
from albums_python.query import album_genre_queries, album_queries, genre_queries
from albums_python.service.jwt import jwt_required
from albums_python.service.models.album_genre_schemas import (
    AlbumGenreResponse,
    AlbumGenreResponseSchema,
)
from albums_python.service.models.http import Response

album_genres_blueprint = Blueprint("album_genres", __name__)


@album_genres_blueprint.get("/albums/<int:album_id>/genres")
def show(album_id: int) -> Union[Response, list[Response]]:
    album = album_queries.get_album_by_id(album_id)

    if album is None:
        return dict(message=f"Album<{album_id}> not found"), 404

    album_genres = album_genre_queries.get_genres_for_albums([album])
    genres = genre_queries.get_genres_by_id(
        genre_ids=[album_genre.genre.id for album_genre in album_genres]
    )
    genres_dict = {genre.id: genre for genre in genres}

    return [
        AlbumGenreResponseSchema.dump(
            AlbumGenreResponse.from_album_genre(album_genre, genres_dict[album_genre.genre.id])
        )
        for album_genre in album_genres
    ]


@album_genres_blueprint.post("/albums/<int:album_id>/genres/<int:genre_id>")
@jwt_required
def create(album_id: int, genre_id: int, user_id: int) -> Response:
    album = album_queries.get_album_by_id(album_id)

    if album is None:
        return dict(message=f"Album<{album_id}> not found"), 404

    genres = genre_queries.get_genres_by_id([genre_id])

    if not genres:
        return dict(message=f"Genre<{genre_id}> not found"), 404

    genre, *_ = genres

    if is_album_already_associated_with_genre(album, genre):
        return (
            dict(message=f"Album<{album_id}> is already associated with Genre<{genre_id}>"),
            400,
        )

    association = album_genre_queries.add_genre_to_album(album, genre)
    albums_domain.search_albums.cache_clear()

    return (
        AlbumGenreResponseSchema.dump(
            AlbumGenreResponse.from_album_genre(album_genre=association, genre=genre)
        ),
        201,
    )


@album_genres_blueprint.delete("/album_genres/<int:album_genre_id>")
@jwt_required
def delete(album_genre_id: int, user_id: int) -> Response:
    association = album_genre_queries.get_album_genre_association_by_id(album_genre_id)

    if association is None:
        return dict(message=f"AlbumGenre<{album_genre_id}> not found"), 404

    album_genre_queries.remove_album_genre_association(association)
    albums_domain.search_albums.cache_clear()
    return dict()
