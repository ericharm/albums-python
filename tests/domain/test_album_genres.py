from faker import Faker

from albums_python.domain.album_genres import is_album_already_associated_with_genre
from albums_python.query import album_genre_queries, album_queries, genre_queries


def test_is_album_already_associated_with_genre(faker: Faker) -> None:
    album = album_queries.create_album(
        artist="The Rolling Stones",
        title="Sticky Fingers",
        released="1971",
        format="LP",
        label="Rolling Stones",
        notes=None,
    )

    rock = genre_queries.create_genre(name=faker.word())
    assert is_album_already_associated_with_genre(album, rock) is False

    album_genre_queries.add_genre_to_album(album=album, genre=rock)
    assert is_album_already_associated_with_genre(album, rock) is True
