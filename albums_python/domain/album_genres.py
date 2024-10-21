from albums_python.query.models.album import Album
from albums_python.query.models.genre import Genre


def is_album_already_associated_with_genre(album: Album, genre: Genre) -> bool:
    return genre.id in [g.id for g in album.genres]
