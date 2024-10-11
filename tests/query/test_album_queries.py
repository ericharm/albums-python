from freezegun import freeze_time

from albums_python.domain.utils import current_utc_datetime
from albums_python.query import album_queries
from albums_python.query.models.album import Album
from tests.utils.albums import create_test_album
from tests.utils.base import clear_table, database_model_to_dict


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

        assert database_model_to_dict(album) == dict(
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


def test_get_album_by_id() -> None:
    now = current_utc_datetime()
    album_id = 0

    with freeze_time(now):
        album = create_test_album(
            artist="The Beatles",
            title="Abbey Road",
            released="1969",
            format="LP",
            label="Apple",
            notes=None,
        )
        album_id = album.id

    album = album_queries.get_album_by_id(album_id)
    assert album is not None

    assert database_model_to_dict(album) == dict(
        id=album_id,
        artist="The Beatles",
        title="Abbey Road",
        released="1969",
        format="LP",
        label="Apple",
        notes=None,
        created_at=now.replace(tzinfo=None),
        updated_at=now.replace(tzinfo=None),
    )


def test_get_albums() -> None:
    clear_table(Album)

    now = current_utc_datetime()
    album_id = 0

    with freeze_time(now):
        album = create_test_album(
            artist="The Beatles",
            title="Abbey Road",
            released="1969",
            format="LP",
            label="Apple",
            notes=None,
        )
        album_id = album.id

    albums = album_queries.get_albums()
    assert len(albums) == 1
    album, *_ = albums

    assert database_model_to_dict(album) == dict(
        id=album_id,
        artist="The Beatles",
        title="Abbey Road",
        released="1969",
        format="LP",
        label="Apple",
        notes=None,
        created_at=now.replace(tzinfo=None),
        updated_at=now.replace(tzinfo=None),
    )
