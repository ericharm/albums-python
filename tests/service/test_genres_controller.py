from faker import Faker

from albums_python.query import genre_queries
from albums_python.query.models.genre import Genre
from tests.conftest import TestClient
from tests.utils.base import clear_table


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
