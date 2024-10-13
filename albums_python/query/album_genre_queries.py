from albums_python.query.models.album import Album
from albums_python.query.models.album_genre import AlbumGenre
from albums_python.query.models.genre import Genre


def add_genre_to_album(album: Album, genre: Genre) -> None:
    AlbumGenre.create(album=album, genre=genre)
