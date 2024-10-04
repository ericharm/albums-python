from typing import Optional

from sqlalchemy import Sequence, select
from sqlalchemy.orm import Session

from albums_python.domain.database import get_database
from albums_python.query.models.album import Album


def get_albums() -> Sequence[Album]:
    engine = get_database()
    with Session(engine) as session:
        albums = session.execute(select(Album)).scalars().all()
        return albums


def get_album_by_id(album_id: int) -> Optional[Album]:
    engine = get_database()
    with Session(engine) as session:
        statement = select(Album).filter(Album.id == album_id)
        album = session.execute(statement).scalar()
        return album
