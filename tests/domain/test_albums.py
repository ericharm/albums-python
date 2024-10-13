from unittest.mock import ANY

from freezegun import freeze_time

from albums_python.domain import albums as albums_domain
from albums_python.domain.utils import current_utc_datetime
from albums_python.query.models.album import Album
from albums_python.service.models.album_schemas import AlbumResponse, AlbumsIndexResponse
from tests.utils.albums import create_test_album
from tests.utils.base import clear_table


def test_get_albums_page() -> None:
    clear_table(Album)

    for _ in range(5):
        create_test_album()

    now = current_utc_datetime()
    with freeze_time(now):
        create_test_album(
            artist='"Weird Al" Yankovic',
            title="Bad Hair Day",
            format="CD",
            released="1996",
            label="Scotti Bros.",
        )

    albums_page = albums_domain.get_albums_page(page=2, page_size=5)
    assert albums_page == AlbumsIndexResponse(
        page=2, page_size=5, total_pages=2, total_count=6, albums=ANY
    )
    assert len(albums_page.albums) == 1

    bad_hair_day, *_ = albums_page.albums
    assert bad_hair_day == AlbumResponse(
        id=6,
        artist='"Weird Al" Yankovic',
        released="1996",
        title="Bad Hair Day",
        format="CD",
        label="Scotti Bros.",
        created_at=now,
        updated_at=now,
        notes=None,
        genres=[],
    )
