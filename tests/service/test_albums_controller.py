from unittest.mock import ANY, patch

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
        response = c.get("/albums")
        assert response.status_code == 200
        assert response.json == dict(
            albums=[
                dict(
                    id=1,
                    artist="Gorillaz",
                    title="Demon Days",
                    released="2005",
                    format="LP",
                    label="Parlophone",
                    notes=None,
                    created_at=now.replace(tzinfo=None).isoformat(),
                    updated_at=now.replace(tzinfo=None).isoformat(),
                )
            ]
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
            created_at=now.replace(tzinfo=None).isoformat(),
            updated_at=now.replace(tzinfo=None).isoformat(),
        )


def test_create_album(client: TestClient) -> None:
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
        assert response.json == dict(
            id=ANY,
            artist="The Velvet Underground",
            title="The Velvet Underground & Nico",
            released="1967",
            format="LP",
            label="Verve",
            notes=None,
            created_at=now.isoformat(),
            updated_at=now.isoformat(),
        )
