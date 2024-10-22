from flask import Blueprint

from albums_python.query import genre_queries
from albums_python.service.models.genre_schemas import GenreResponseSchema
from albums_python.service.models.http import Response

genres_blueprint = Blueprint("genres", __name__)


@genres_blueprint.get("/genres")
def index() -> Response:
    all_genres = genre_queries.get_all_genres()
    return [GenreResponseSchema.dump(genre) for genre in all_genres]
