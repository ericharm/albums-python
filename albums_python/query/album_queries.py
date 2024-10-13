from typing import Optional

from sqlalchemy.orm import Session, subqueryload

from albums_python.query.models.album import Album
from albums_python.query.session import use_session


@use_session
def create_album(
    artist: Optional[str],
    released: Optional[str],
    title: str,
    format: Optional[str],
    label: Optional[str],
    notes: Optional[str],
    session: Optional[Session] = None,
) -> Album:
    assert session
    album = Album(
        artist=artist,
        released=released,
        title=title,
        format=format,
        label=label,
        notes=notes,
    )

    session.add(album)
    session.commit()
    return album


@use_session
def get_album_by_id(album_id: int, session: Optional[Session] = None) -> Optional[Album]:
    assert session
    album = session.query(Album).options(subqueryload(Album.genres)).filter_by(id=album_id).first()
    return album


@use_session
def get_albums_page(
    page: int = 1, page_size: int = 10, session: Optional[Session] = None
) -> list[Album]:
    assert session
    offset = (page - 1) * page_size
    return list(session.query(Album).offset(offset).limit(page_size).all())


@use_session
def get_albums_count(session: Optional[Session] = None) -> int:
    assert session
    return session.query(Album).count()
