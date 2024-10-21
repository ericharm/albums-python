from faker import Faker
from freezegun import freeze_time

from albums_python.domain.users import _generate_jwt
from albums_python.domain.utils import current_utc_datetime
from albums_python.query import album_genre_queries, album_queries, genre_queries
from albums_python.query.models.album import Album
from albums_python.query.models.album_genre import AlbumGenre
from albums_python.query.models.genre import Genre
from tests.conftest import TestClient
from tests.utils.base import clear_table
from tests.utils.users import create_test_user


def test_show_genre_associations_for_album(faker: Faker, client: TestClient) -> None:
    album = album_queries.create_album(
        artist="Prince",
        title="Batman",
        released="1989",
        format="LP",
        label="Warner Bros.",
        notes="",
    )

    funk = genre_queries.create_genre(name=faker.word())
    soul = genre_queries.create_genre(name=faker.word())

    funk_association = album_genre_queries.add_genre_to_album(album=album, genre=funk)
    soul_association = album_genre_queries.add_genre_to_album(album=album, genre=soul)

    with client() as c:
        response = c.get(f"/albums/{album.id}/genres")
        assert response.status_code == 200

        assert response.json == [
            dict(
                id=funk_association.id,
                album_id=album.id,
                genre_id=funk.id,
                genre_name=funk.name,
            ),
            dict(
                id=soul_association.id,
                album_id=album.id,
                genre_id=soul.id,
                genre_name=soul.name,
            ),
        ]


def test_create_album_genre_association_success(faker: Faker, client: TestClient) -> None:
    user = create_test_user()
    jwt, _ = _generate_jwt(str(user.id))
    now = current_utc_datetime()

    with freeze_time(now):
        album = album_queries.create_album(
            artist="The Band",
            title="Music from Big Pink",
            released="1968",
            format="LP",
            label="Capitol",
            notes=None,
        )
        assert album.genres == []

    americana = genre_queries.create_genre(name=faker.word())

    response = client().post(
        f"/albums/{album.id}/genres/{americana.id}",
        headers=dict(Authorization=f"Bearer {jwt}"),
    )
    assert response.status_code == 201
    assert response.json
    assert response.json == dict(
        id=response.json["id"],
        album_id=album.id,
        genre_id=americana.id,
        genre_name=americana.name,
    )

    music_from_big_pink = album_queries.get_album_by_id(album.id)
    assert music_from_big_pink is not None
    assert [genre.to_dict() for genre in music_from_big_pink.genres] == [
        dict(
            id=americana.id,
            name=americana.name,
        )
    ]


def test_create_album_genre_association_album_doesnt_exist(
    faker: Faker, client: TestClient
) -> None:
    clear_table(Album)
    user = create_test_user()
    jwt, _ = _generate_jwt(str(user.id))
    album_id = faker.random_int()

    americana = genre_queries.create_genre(name=faker.word())

    response = client().post(
        f"/albums/{album_id}/genres/{americana.id}",
        headers=dict(Authorization=f"Bearer {jwt}"),
    )

    assert response.status_code == 404
    assert response.json
    assert response.json == dict(message=f"Album<{album_id}> not found")


def test_create_album_genre_association_genre_doesnt_exist(
    faker: Faker, client: TestClient
) -> None:
    clear_table(Genre)
    user = create_test_user()
    jwt, _ = _generate_jwt(str(user.id))
    now = current_utc_datetime()

    with freeze_time(now):
        album = album_queries.create_album(
            artist="Ramones",
            title="Ramones",
            released="1976",
            format="LP",
            label="Sire",
            notes=None,
        )

    genre_id = faker.random_int()

    response = client().post(
        f"/albums/{album.id}/genres/{genre_id}",
        headers=dict(Authorization=f"Bearer {jwt}"),
    )

    assert response.status_code == 404
    assert response.json
    assert response.json == dict(message=f"Genre<{genre_id}> not found")


def test_create_album_genre_association_already_exists(faker: Faker, client: TestClient) -> None:
    clear_table(Genre)
    clear_table(AlbumGenre)

    user = create_test_user()
    jwt, _ = _generate_jwt(str(user.id))

    album = album_queries.create_album(
        artist="Metallica",
        title="Master of Puppets",
        released="1986",
        format="LP",
        label="Elektra",
        notes=None,
    )

    metal = genre_queries.create_genre(name=faker.word())
    album_genre_queries.add_genre_to_album(album=album, genre=metal)

    response = client().post(
        f"/albums/{album.id}/genres/{metal.id}",
        headers=dict(Authorization=f"Bearer {jwt}"),
    )

    assert response.status_code == 400
    assert response.json
    assert response.json == dict(
        message=f"Album<{album.id}> is already associated with Genre<{metal.id}>"
    )


def test_delete_album_genre_association_success(faker: Faker, client: TestClient) -> None:
    user = create_test_user()
    jwt, _ = _generate_jwt(str(user.id))

    album = album_queries.create_album(
        artist="Alanis Morissette",
        title="Jagged Little Pill",
        released="1995",
        format="LP",
        label="Maverick",
        notes=None,
    )

    rock = genre_queries.create_genre(name=faker.word())
    association = album_genre_queries.add_genre_to_album(album=album, genre=rock)

    response = client().delete(
        f"/album_genres/{association.id}", headers=dict(Authorization=f"Bearer {jwt}")
    )
    assert response.status_code == 200
    assert response.json == dict()

    jagged_little_pill = album_queries.get_album_by_id(album.id)
    assert jagged_little_pill is not None
    assert jagged_little_pill.genres == []


def test_delete_album_genre_association_doesnt_exist(faker: Faker, client: TestClient) -> None:
    user = create_test_user()
    jwt, _ = _generate_jwt(str(user.id))
    association_id = faker.random_int()

    album = album_queries.create_album(
        artist="Miles Davis",
        title="Kind of Blue",
        released="1959",
        format="LP",
        label="Columbia",
        notes=None,
    )

    response = client().delete(
        f"/album_genres/{association_id}", headers=dict(Authorization=f"Bearer {jwt}")
    )
    assert response.status_code == 404
    assert response.json
    assert response.json == dict(message=f"AlbumGenre<{association_id}> not found")
