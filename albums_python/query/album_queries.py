from typing import Optional

from sqlalchemy.orm import Session

from albums_python.client.database import get_db_session
from albums_python.query.models.album import Album
from albums_python.query.session import use_session


@use_session
def get_albums_count(session: Optional[Session] = None) -> int:
    assert session is not None
    return session.query(Album).count()


@use_session
def get_albums_page(
    page: int = 1, page_size: int = 10, session: Optional[Session] = None
) -> list[Album]:
    assert session is not None
    offset = (page - 1) * page_size
    return list(session.query(Album).offset(offset).limit(page_size).all())


def get_album_by_id(album_id: int) -> Optional[Album]:
    with get_db_session() as session:
        return session.get(Album, album_id)


def create_album(
    artist: Optional[str],
    released: Optional[str],
    title: str,
    format: Optional[str],
    label: Optional[str],
    notes: Optional[str],
) -> Album:
    album = Album(
        artist=artist,
        released=released,
        title=title,
        format=format,
        label=label,
        notes=notes,
    )

    return album.save()
