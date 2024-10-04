from typing import Union

from flask import Blueprint

from albums_python.query import albums as albums_queries
from albums_python.service.models.albums import (
    AlbumResponse,
    AlbumResponseSchema,
    AlbumsIndexResponse,
    AlbumsIndexResponseSchema,
)

albums_blueprint = Blueprint("albums", __name__)

Response = Union[dict, tuple[dict, int]]


@albums_blueprint.get("/albums")
def index() -> Response:
    all_albums = albums_queries.get_albums()

    return AlbumsIndexResponseSchema.dump(
        AlbumsIndexResponse(albums=[AlbumResponse.from_album(album) for album in all_albums])
    )


@albums_blueprint.get("/albums/<album_id>")
def show(album_id: int) -> Response:
    album = albums_queries.get_album_by_id(album_id)

    if album is None:
        return dict(message=f"Album<{album_id} not found"), 404

    return AlbumResponseSchema.dump(AlbumResponse.from_album(album))
