from peewee import prefetch

from albums_python.query import album_genre_queries, album_queries, genre_queries
from albums_python.service.models.album_schemas import AlbumResponse, AlbumsIndexResponse


def get_albums_page(page: int = 1, page_size: int = 10) -> AlbumsIndexResponse:
    total_count = album_queries.get_albums_count()
    total_pages = (total_count + page_size - 1) // page_size

    albums = album_queries.get_albums_page(page=page, page_size=page_size)
    album_genres = album_genre_queries.get_genres_for_albums(albums=albums)

    genres = genre_queries.get_genres_by_id(
        genre_ids=[album_genre.genre for album_genre in album_genres]
    )
    albums_with_genres = prefetch(albums, album_genres, genres)

    return AlbumsIndexResponse(
        page=page,
        page_size=page_size,
        total_pages=total_pages,
        total_count=total_count,
        albums=[AlbumResponse.from_album(album) for album in albums_with_genres],
    )
