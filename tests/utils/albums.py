from typing import Any

from faker import Faker

from albums_python.query.models.album import Album


def create_test_album(**kwargs: Any) -> Album:
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

    album.save()
    return album
