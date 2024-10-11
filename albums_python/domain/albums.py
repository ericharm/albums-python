from albums_python.client.database import get_db_session
from albums_python.query import album_queries
from albums_python.service.models.album_schemas import AlbumResponse, AlbumsIndexResponse


def get_albums_page(page: int = 1, page_size: int = 10) -> AlbumsIndexResponse:
    with get_db_session() as session:
        total_count = album_queries.get_albums_count(session=session)
        albums_page = album_queries.get_albums_page(page=page, page_size=page_size, session=session)

    total_pages = (total_count + page_size - 1) // page_size

    return AlbumsIndexResponse(
        page=page,
        page_size=page_size,
        total_pages=total_pages,
        total_count=total_count,
        albums=[AlbumResponse.from_album(album) for album in albums_page],
    )
