from flask import Blueprint
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
@use_args(PaginatedRequestSchema)
def index(page_data: PaginatedRequest) -> Response:
    result = albums_domain.get_albums_page(page=page_data.page, page_size=page_data.page_size)
    return AlbumsIndexResponseSchema.dump(result)


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
