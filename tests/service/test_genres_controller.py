from faker import Faker
from freezegun import freeze_time

from albums_python.domain.users import _generate_jwt
from albums_python.domain.utils import current_utc_datetime
from albums_python.query import genre_queries
from albums_python.query.models.genre import Genre
from tests.conftest import TestClient
from tests.utils.base import clear_table
from tests.utils.users import create_test_user


def test_albums_index(faker: Faker, client: TestClient) -> None:
    clear_table(Genre)

    disco = genre_queries.create_genre(name=faker.word())
    jazz = genre_queries.create_genre(name=faker.word())
    punk = genre_queries.create_genre(name=faker.word())

    with client() as c:
        response = c.get("/genres")
        assert response.status_code == 200
        assert response.json
        sorted_genres = sorted(response.json, key=lambda genre: genre["id"])
        assert sorted_genres == [
            dict(id=disco.id, name=disco.name),
            dict(id=jazz.id, name=jazz.name),
            dict(id=punk.id, name=punk.name),
        ]


def test_create_genre(client: TestClient) -> None:
    user = create_test_user()
    jwt, _ = _generate_jwt(str(user.id))
    now = current_utc_datetime()
    genre_id = 0

    with freeze_time(now), client() as c:
        response = c.post(
            "/genres",
            json=dict(name="Cuddlecore"),
            headers=dict(Authorization=f"Bearer {jwt}"),
        )
        assert response.status_code == 201
        assert response.json
        genre_id = response.json["id"]
        assert response.json == dict(id=genre_id, name="Cuddlecore")

    queried_genre, *_ = genre_queries.get_genres_by_id(genre_ids=[genre_id])
    assert queried_genre.to_dict() == dict(id=genre_id, name="Cuddlecore")
