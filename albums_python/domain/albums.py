from typing import Optional, cast

from peewee import prefetch

from albums_python.query import album_genre_queries, album_queries, genre_queries
from albums_python.service.models.album_schemas import AlbumResponse, AlbumsIndexResponse


def search_albums(query: Optional[str], page: int, page_size: int) -> AlbumsIndexResponse:
    album_select = (
        album_queries.get_albums()
        if query is None
        else album_queries.fuzzy_search_albums(query_string=query)
    )
    total_count = len(album_select)
    total_pages = (total_count + page_size - 1) // page_size

    albums = album_select.paginate(page, page_size)

    album_genres = album_genre_queries.get_genres_for_albums(albums=list(albums))
    genres = genre_queries.get_genres_by_id(
        genre_ids=[cast(int, album_genre.genre) for album_genre in album_genres]
    )
    albums_with_genres = prefetch(albums, album_genres, genres)

    return AlbumsIndexResponse(
        page=page,
        page_size=page_size,
        total_pages=total_pages,
        total_count=total_count,
        albums=[AlbumResponse.from_album(album) for album in albums_with_genres],
    )
