from albums_python.client.database import get_db_session
from albums_python.query.models.album import Album
from albums_python.query.models.genre import Genre


def add_genre_to_album(album: Album, genre: Genre) -> None:
    with get_db_session() as session:
        album = session.merge(album)
        genre = session.merge(genre)
        album.genres.append(genre)
        session.commit()
