from typing import Optional

from sqlalchemy.orm import Session

from albums_python.query.models.genre import Genre
from albums_python.query.session import use_session


@use_session
def create_genre(
    name: str,
    session: Optional[Session] = None,
) -> Genre:
    assert session
    genre = Genre(
        name=name,
    )

    session.add(genre)
    session.commit()
    return genre
