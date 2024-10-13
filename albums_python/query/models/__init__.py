from albums_python.query.models.album import Album  # noqa: F401
from albums_python.query.models.album_genre import AlbumGenre  # noqa: F401
from albums_python.query.models.genre import Genre  # noqa: F401
from albums_python.query.models.user import User  # noqa: F401

TABLES = [Album, Genre, AlbumGenre, User]
