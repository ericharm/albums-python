from albums_python.query.models.album import Album
from albums_python.query.models.album_genre import AlbumGenre
from albums_python.query.models.genre import Genre


def add_genre_to_album(album: Album, genre: Genre) -> None:
    AlbumGenre.create(album=album, genre=genre)


def get_genres_for_albums(albums: list[Album]) -> list[AlbumGenre]:
    album_ids = [album.id for album in albums]
    return AlbumGenre.select().where(AlbumGenre.album.in_(album_ids))  # type: ignore
