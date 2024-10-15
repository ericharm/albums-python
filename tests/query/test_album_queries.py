from faker import Faker
from freezegun import freeze_time

from albums_python.defs.constants import DEFAULT_NONE
from albums_python.domain.utils import current_utc_datetime
from albums_python.query import album_queries
from albums_python.query.models.album import Album
from tests.utils.base import clear_table


def test_create_album() -> None:
    now = current_utc_datetime()

    with freeze_time(now):
        album = album_queries.create_album(
            artist="John Prine",
            released="1978",
            title="Bruised Orange",
            format="LP",
            label="Asylum",
            notes=None,
        )

        assert album is not None
        assert album.id is not None

        assert album.to_dict() == dict(
            id=album.id,
            artist="John Prine",
            title="Bruised Orange",
            released="1978",
            format="LP",
            label="Asylum",
            notes=None,
            created_at=now,
            updated_at=now,
        )


def test_update_album() -> None:
    then = current_utc_datetime()
    album_id = 0

    with freeze_time(then):
        album = album_queries.create_album(
            artist="George Harrison",
            title="All Things Must Pass",
            released="1970",
            format="LP",
            label="Apple",
            notes=None,
        )
        album_id = album.id

    now = current_utc_datetime()
    with freeze_time(now):
        album = album_queries.update_album(
            album=album,
            artist=DEFAULT_NONE,
            title=DEFAULT_NONE,
            released=DEFAULT_NONE,
            format=DEFAULT_NONE,
            label=DEFAULT_NONE,
            notes="A triple album",
        )

    album = album_queries.get_album_by_id(album_id)
    assert album is not None
    assert album.to_dict() == dict(
        id=album_id,
        artist="George Harrison",
        title="All Things Must Pass",
        released="1970",
        format="LP",
        label="Apple",
        notes="A triple album",
        created_at=then,
        updated_at=now,
    )


def test_get_album_by_id() -> None:
    now = current_utc_datetime()
    album_id = 0

    with freeze_time(now):
        album = album_queries.create_album(
            artist="Meat Loaf",
            title="Bat Out of Hell",
            released="1977",
            format="LP",
            label="Epic",
            notes=None,
        )
        album_id = album.id

    album = album_queries.get_album_by_id(album_id)
    assert album is not None

    assert album.to_dict() == dict(
        id=album_id,
        artist="Meat Loaf",
        title="Bat Out of Hell",
        released="1977",
        format="LP",
        label="Epic",
        notes=None,
        created_at=now,
        updated_at=now,
    )


def test_get_albums_count(faker: Faker) -> None:
    clear_table(Album)

    for _ in range(8):
        album_queries.create_album(
            artist=faker.text(),
            title=faker.text(),
            released=faker.year(),
            format="LP",
            label=faker.text(),
            notes=None,
        )

    assert album_queries.get_albums_count() == 8


def test_get_albums_page() -> None:
    clear_table(Album)

    now = current_utc_datetime()
    album_id = 0

    with freeze_time(now):
        album = album_queries.create_album(
            artist="The Beatles",
            title="Abbey Road",
            released="1969",
            format="LP",
            label="Apple",
            notes=None,
        )
        album_id = album.id

    albums = album_queries.get_albums_page(page=1, page_size=10)
    assert len(albums) == 1
    album, *_ = albums

    assert album.to_dict() == dict(
        id=album_id,
        artist="The Beatles",
        title="Abbey Road",
        released="1969",
        format="LP",
        label="Apple",
        notes=None,
        created_at=now,
        updated_at=now,
    )
