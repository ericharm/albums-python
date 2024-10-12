from albums_python.query import genre_queries


def test_create_genre() -> None:
    genre = genre_queries.create_genre(
        name="Rock",
    )

    assert genre.to_dict() == dict(id=genre.id, name="Rock")
