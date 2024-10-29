from flask import Blueprint
from webargs.flaskparser import use_args

from albums_python.query import genre_queries
from albums_python.service.jwt import jwt_required
from albums_python.service.models.genre_schemas import (
    CreateGenreRequest,
    CreateGenreRequestSchema,
    GenreResponseSchema,
)
from albums_python.service.models.http import Response

genres_blueprint = Blueprint("genres", __name__)


@genres_blueprint.get("/genres")
def index() -> list[Response]:
    all_genres = genre_queries.get_all_genres()
    return [GenreResponseSchema.dump(genre) for genre in all_genres]


@genres_blueprint.post("/genres")
@jwt_required
@use_args(CreateGenreRequestSchema)
def create(request: CreateGenreRequest, user_id: int) -> Response:
    genre = genre_queries.create_genre(name=request.name)
    return GenreResponseSchema.dump(genre), 201
