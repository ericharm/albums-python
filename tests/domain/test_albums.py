from unittest.mock import ANY

from faker import Faker
from freezegun import freeze_time

from albums_python.domain import albums as albums_domain
from albums_python.domain.utils import current_utc_datetime
from albums_python.query import album_queries
from albums_python.query.models.album import Album
from albums_python.service.models.album_schemas import (
    AlbumRequest,
    AlbumResponse,
    AlbumsIndexResponse,
)
from tests.utils.base import clear_table


def test_get_albums_page(faker: Faker) -> None:
    clear_table(Album)

    for n in range(5):
        # The albums will be sorted alphabetically by artist,
        # so we'll make the results more deterministic by
        # prepending the artist name with a number.
        album_queries.create_album(
            artist=f"{n} {faker.word()}s",
            title=faker.text(),
            released=faker.year(),
            format="LP",
            label=faker.text(),
            notes=None,
        )

    now = current_utc_datetime()
    with freeze_time(now):
        album_queries.create_album(
            artist="Weird Al Yankovic",
            title="Bad Hair Day",
            released="1996",
            format="CD",
            label="Scotti Bros.",
            notes=None,
        )

    albums_page = albums_domain.get_albums_page(page=2, page_size=5)
    assert albums_page == AlbumsIndexResponse(
        page=2, page_size=5, total_pages=2, total_count=6, albums=ANY
    )
    assert len(albums_page.albums) == 1

    bad_hair_day, *_ = albums_page.albums
    assert bad_hair_day == AlbumResponse(
        id=bad_hair_day.id,
        artist="Weird Al Yankovic",
        released="1996",
        title="Bad Hair Day",
        format="CD",
        label="Scotti Bros.",
        created_at=now,
        updated_at=now,
        notes=None,
        genres=[],
    )


def test_update_album_from_request() -> None:
    then = current_utc_datetime()
    album_id = 0

    with freeze_time(then):
        album = album_queries.create_album(
            artist="Bob Dylan",
            title="Blonde on Blonde",
            released=None,
            format="LP",
            label=None,
            notes=None,
        )
        album_id = album.id

    now = current_utc_datetime()
    with freeze_time(now):
        album = albums_domain.update_album_from_request(
            album_id=album.id,
            request=AlbumRequest(
                artist="Bob Dylan",
                title="Blonde on Blonde",
                released="1966",
                format="LP",
                label="Columbia",
                notes=None,
            ),
        )

    assert album is not None
    assert album.to_dict() == dict(
        id=album_id,
        artist="Bob Dylan",
        title="Blonde on Blonde",
        released="1966",
        format="LP",
        label="Columbia",
        notes=None,
        created_at=then,
        updated_at=now,
    )


def test_update_album_from_request_not_found() -> None:
    album = albums_domain.update_album_from_request(
        album_id=0,
        request=AlbumRequest(
            artist="Aretha Franklin",
            title="I Never Loved a Man the Way I Love You",
            released="1967",
            format="LP",
            label="Atlantic",
            notes=None,
        ),
    )

    assert album is None
