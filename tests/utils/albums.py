from typing import Any, Optional

from faker import Faker
from sqlalchemy.orm import Session

from albums_python.query.models.album import Album
from albums_python.query.session import use_session


@use_session
def create_test_album(session: Optional[Session] = None, **kwargs: Any) -> Album:
    assert session
    fake = Faker()

    album = Album(
        artist=fake.text(),
        title=fake.text(),
        released=fake.year(),
        format="LP",
        label=fake.text(),
        notes=None,
    )

    for key, value in kwargs.items():
        setattr(album, key, value)

    session.add(album)
    session.commit()
    return album
