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
)
from albums_python.service.models.http import PaginatedRequest, PaginatedRequestSchema, Response

albums_blueprint = Blueprint("albums", __name__)


@albums_blueprint.get("/albums")
def index() -> Response:
    page_data: PaginatedRequest = PaginatedRequestSchema.load(request.args)
    result = albums_domain.get_albums_page(page=page_data.page, page_size=page_data.page_size)
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
    album = albums_domain.update_album_from_request(album_id, request)

    if album is None:
        return dict(message=f"Album<{album_id} not found"), 404

    return AlbumResponseSchema.dump(AlbumResponse.from_album(album))
