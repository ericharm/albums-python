from typing import Optional

from peewee import DoesNotExist

from albums_python.query.models.album import Album
from albums_python.query.models.album_genre import AlbumGenre
from albums_python.query.models.genre import Genre


def add_genre_to_album(album: Album, genre: Genre) -> AlbumGenre:
    return AlbumGenre.create(album=album, genre=genre)


def get_album_genre_association_by_id(album_genre_id: int) -> Optional[AlbumGenre]:
    try:
        return AlbumGenre.get_by_id(album_genre_id)
    except DoesNotExist:
        return None


def remove_album_genre_association(album_genre: AlbumGenre) -> None:
    album_genre.delete_instance()


def get_genres_for_albums(albums: list[Album]) -> list[AlbumGenre]:
    album_ids = [album.id for album in albums]
    return AlbumGenre.select().where(AlbumGenre.album.in_(album_ids))  # type: ignore
