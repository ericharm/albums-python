from typing import Optional

from sqlalchemy import select

from albums_python.client.database import get_db_session
from albums_python.query.models.album import Album


def get_albums() -> list[Album]:
    with get_db_session() as session:
        return list(session.execute(select(Album)).scalars().all())


def get_album_by_id(album_id: int) -> Optional[Album]:
    with get_db_session() as session:
        return session.execute(select(Album).filter(Album.id == album_id)).scalar()


def create_album(
    artist: Optional[str],
    released: Optional[str],
    title: str,
    format: Optional[str],
    label: Optional[str],
    notes: Optional[str],
) -> Album:
    album = Album(
        artist=artist, released=released, title=title, format=format, label=label, notes=notes
    )

    return album.save()
