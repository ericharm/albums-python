from unittest.mock import patch

from freezegun import freeze_time

from albums_python.domain.users import _generate_jwt
from albums_python.domain.utils import current_utc_datetime
from albums_python.query import album_queries
from albums_python.query.models.album import Album
from tests.conftest import TestClient
from tests.utils.base import clear_table
from tests.utils.users import create_test_user


def test_albums_index(client: TestClient) -> None:
    clear_table(Album)
    now = current_utc_datetime()

    with freeze_time(now):
        album_queries.create_album(
            artist="Gorillaz",
            title="Demon Days",
            released="2005",
            format="LP",
            label="Parlophone",
            notes=None,
        )

    with patch("albums_python.service.albums_controller"), client() as c:
        response = c.get("/albums", query_string=dict(page=1, page_size=10))
        assert response.status_code == 200
        assert response.json == dict(
            page=1,
            page_size=10,
            total_pages=1,
            total_count=1,
            albums=[
                dict(
                    id=1,
                    artist="Gorillaz",
                    title="Demon Days",
                    released="2005",
                    format="LP",
                    label="Parlophone",
                    notes=None,
                    genres=[],
                    created_at=now.isoformat(),
                    updated_at=now.isoformat(),
                )
            ],
        )


def test_show_album(client: TestClient) -> None:
    now = current_utc_datetime()
    album_id = None

    with freeze_time(now):
        album = album_queries.create_album(
            artist="Television",
            title="Marquee Moon",
            released="1977",
            format="LP",
            label="Elektra",
            notes=None,
        )
        album_id = album.id

    with client() as c:
        response = c.get(f"/albums/{album_id}")
        assert response.status_code == 200
        assert response.json == dict(
            id=album_id,
            artist="Television",
            title="Marquee Moon",
            released="1977",
            format="LP",
            label="Elektra",
            notes=None,
            genres=[],
            created_at=now.isoformat(),
            updated_at=now.isoformat(),
        )


def test_create_album_endpoint(client: TestClient) -> None:
    user = create_test_user()
    jwt = _generate_jwt(str(user.id))
    now = current_utc_datetime()

    with freeze_time(now):
        response = client().post(
            "/albums",
            json=dict(
                artist="The Velvet Underground",
                title="The Velvet Underground & Nico",
                released="1967",
                format="LP",
                label="Verve",
                notes=None,
            ),
            headers=dict(Authorization=f"Bearer {jwt}"),
        )

        assert response.status_code == 201
        assert response.json
        assert response.json == dict(
            id=response.json["id"],
            artist="The Velvet Underground",
            title="The Velvet Underground & Nico",
            released="1967",
            format="LP",
            label="Verve",
            notes=None,
            genres=[],
            created_at=now.isoformat(),
            updated_at=now.isoformat(),
        )


def test_update_album_endpoint(client: TestClient) -> None:
    user = create_test_user()
    then = current_utc_datetime()
    album_id = 0

    with freeze_time(then):
        album = album_queries.create_album(
            artist="Billy Joe",
            title="The Strangler",
            released="1977",
            format="LP",
            label="Columbia",
            notes=None,
        )
        album_id = album.id

    jwt = _generate_jwt(str(user.id))
    now = current_utc_datetime()
    with freeze_time(now):
        response = client().put(
            f"/albums/{album_id}",
            json=dict(
                artist="Billy Joel",
                title="The Stranger",
                released="1977",
                format="LP",
                label="Columbia",
                notes="This is a great album",
            ),
            headers=dict(Authorization=f"Bearer {jwt}"),
        )
        assert response.status_code == 200
        assert response.json
        assert response.json == dict(
            id=album_id,
            artist="Billy Joel",
            title="The Stranger",
            released="1977",
            format="LP",
            label="Columbia",
            notes="This is a great album",
            genres=[],
            created_at=then.isoformat(),
            updated_at=now.isoformat(),
        )


def test_update_album_endpoint_not_found(client: TestClient) -> None:
    user = create_test_user()
    album_id = 0
    jwt = _generate_jwt(str(user.id))

    response = client().put(
        f"/albums/{album_id}",
        json=dict(
            artist="Billy Joel",
            title="The Stranger",
            released="1977",
            format="LP",
            label="Columbia",
            notes="This is a great album",
        ),
        headers=dict(Authorization=f"Bearer {jwt}"),
    )
    assert response.status_code == 404
    assert response.json == dict(message=f"Album<{album_id} not found")


def test_delete_album_endpoint(client: TestClient) -> None:
    user = create_test_user()
    then = current_utc_datetime()
    album_id = 0

    with freeze_time(then):
        album = album_queries.create_album(
            artist="Curtis Mayfield",
            title="Super Fly",
            released="1972",
            format="LP",
            label="Curtom",
            notes=None,
        )
        album_id = album.id

    jwt = _generate_jwt(str(user.id))
    response = client().delete(
        f"/albums/{album_id}",
        headers=dict(Authorization=f"Bearer {jwt}"),
    )

    assert response.status_code == 200
    assert response.json == dict()
    assert album_queries.get_album_by_id(album_id) is None


def test_delete_album_endpoint_not_found(client: TestClient) -> None:
    user = create_test_user()
    album_id = 0

    jwt = _generate_jwt(str(user.id))
    response = client().delete(
        f"/albums/{album_id}",
        headers=dict(Authorization=f"Bearer {jwt}"),
    )

    assert response.status_code == 404
    assert response.json
    assert response.json == dict(message=f"Album<{album_id} not found")
