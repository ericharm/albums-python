from dataclasses import asdict

from flask import Blueprint
from webargs.flaskparser import use_args

from albums_python.query import album_queries
from albums_python.service.decorators.jwt import jwt_required
from albums_python.service.models.album_schemas import (
    AlbumRequest,
    AlbumRequestSchema,
    AlbumResponse,
    AlbumResponseSchema,
    AlbumsIndexResponse,
    AlbumsIndexResponseSchema,
)
from albums_python.service.models.response import Response

albums_blueprint = Blueprint("albums", __name__)


@albums_blueprint.get("/albums")
def index() -> Response:
    all_albums = album_queries.get_albums()

    return AlbumsIndexResponseSchema.dump(
        AlbumsIndexResponse(albums=[AlbumResponse.from_album(album) for album in all_albums])
    )


@albums_blueprint.get("/albums/<album_id>")
def show(album_id: int) -> Response:
    album = album_queries.get_album_by_id(album_id)

    if album is None:
        return dict(message=f"Album<{album_id} not found"), 404

    return AlbumResponseSchema.dump(AlbumResponse.from_album(album))


@albums_blueprint.post("/albums")
@jwt_required
@use_args(AlbumRequestSchema)
def create(_: str, request: AlbumRequest) -> Response:
    album = album_queries.create_album(**AlbumRequestSchema.dump(request))
    return AlbumResponseSchema.dump(AlbumResponse.from_album(album)), 201
