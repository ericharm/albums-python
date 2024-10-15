from albums_python.query import genre_queries
from albums_python.query.models.genre import Genre
from tests.utils.base import clear_table


def test_create_genre() -> None:
    genre = genre_queries.create_genre(
        name="Rock",
    )

    assert genre.to_dict() == dict(id=genre.id, name="Rock")


def test_get_genres_by_id() -> None:
    clear_table(Genre)

    genre_queries.create_genre(
        name="Disco",
    )

    jazz = genre_queries.create_genre(
        name="Jazz",
    )

    all_genres = genre_queries.get_genres_by_id(genre_ids=[jazz.id])

    assert [genre.to_dict() for genre in all_genres] == [
        dict(id=jazz.id, name="Jazz"),
    ]
