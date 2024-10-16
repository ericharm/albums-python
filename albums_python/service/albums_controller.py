from flask import Blueprint, request
from webargs.flaskparser import use_args

from albums_python.domain import albums as albums_domain
from albums_python.query import album_queries
from albums_python.service.jwt import jwt_required
from albums_python.service.models.album_schemas import (
    AlbumRequest,
    AlbumRequestSchema,
    AlbumResponse,
    AlbumResponseSchema,
    AlbumsIndexResponseSchema,
    SearchAlbumsRequest,
    SearchAlbumsRequestSchema,
)
from albums_python.service.models.http import Response

albums_blueprint = Blueprint("albums", __name__)


@albums_blueprint.get("/albums")
def index() -> Response:
    search_albums_request: SearchAlbumsRequest = SearchAlbumsRequestSchema.load(request.args)
    result = albums_domain.search_albums(
        query=search_albums_request.query,
        page=search_albums_request.page,
        page_size=search_albums_request.page_size,
    )
    return AlbumsIndexResponseSchema.dump(result)


@albums_blueprint.get("/albums/<int:album_id>")
def show(album_id: int) -> Response:
    album = album_queries.get_album_by_id(album_id)

    if album is None:
        return dict(message=f"Album<{album_id} not found"), 404

    return AlbumResponseSchema.dump(AlbumResponse.from_album(album))


@albums_blueprint.post("/albums")
@jwt_required
@use_args(AlbumRequestSchema)
def create(request: AlbumRequest, user_id: int) -> Response:
    album = album_queries.create_album(**AlbumRequestSchema.dump(request))
    return AlbumResponseSchema.dump(AlbumResponse.from_album(album)), 201


@albums_blueprint.put("/albums/<int:album_id>")
@jwt_required
@use_args(AlbumRequestSchema)
def update(
    request: AlbumRequest,
    album_id: int,
    user_id: int,
) -> Response:
    album = album_queries.get_album_by_id(album_id)

    if album is None:
        return dict(message=f"Album<{album_id} not found"), 404

    album = album_queries.update_album(album=album, **AlbumRequestSchema.dump(request))
    return AlbumResponseSchema.dump(AlbumResponse.from_album(album))


@albums_blueprint.delete("/albums/<int:album_id>")
@jwt_required
def delete(album_id: int, user_id: int) -> Response:
    album = album_queries.get_album_by_id(album_id)

    if album is None:
        return dict(message=f"Album<{album_id} not found"), 404

    album_queries.delete_album(album)

    return dict(), 200
