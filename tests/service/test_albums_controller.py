from unittest.mock import patch

from freezegun import freeze_time

from albums_python.domain.users import _generate_jwt
from albums_python.domain.utils import current_utc_datetime
from albums_python.query.models.album import Album
from tests.conftest import TestClient
from tests.utils.albums import create_test_album
from tests.utils.base import clear_table
from tests.utils.users import create_test_user


def test_albums_index(client: TestClient) -> None:
    clear_table(Album)
    now = current_utc_datetime()

    with freeze_time(now):
        create_test_album(
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
        album_id = create_test_album(
            artist="Television",
            title="Marquee Moon",
            released="1977",
            format="LP",
            label="Elektra",
            notes=None,
        ).id

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
