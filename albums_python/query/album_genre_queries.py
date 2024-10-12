from typing import Optional

from sqlalchemy.orm import Session

from albums_python.query.models.album import Album
from albums_python.query.models.genre import Genre
from albums_python.query.session import use_session


@use_session
def add_genre_to_album(album: Album, genre: Genre, session: Optional[Session] = None) -> None:
    assert session
    album.genres.append(genre)
    session.commit()
