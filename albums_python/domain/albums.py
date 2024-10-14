from albums_python.query import album_queries
from albums_python.service.models.album_schemas import AlbumResponse, AlbumsIndexResponse


def get_albums_page(page: int = 1, page_size: int = 10) -> AlbumsIndexResponse:
    total_count = album_queries.get_albums_count()
    albums_page = album_queries.get_albums_page(page=page, page_size=page_size)
    total_pages = (total_count + page_size - 1) // page_size

    return AlbumsIndexResponse(
        page=page,
        page_size=page_size,
        total_pages=total_pages,
        total_count=total_count,
        albums=[AlbumResponse.from_album(album) for album in albums_page],
    )
