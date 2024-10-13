from albums_python.query import album_genre_queries, genre_queries
from tests.utils.albums import create_test_album


def test_add_genre_to_album() -> None:
    fear_of_music = create_test_album(
        artist="Talking Heads",
        title="Fear of Music",
        released="1979",
        format="LP",
        label="Sire",
        notes=None,
    )

    new_wave = genre_queries.create_genre("New Wave")

    album_genre_queries.add_genre_to_album(fear_of_music, new_wave)
    assert [genre.name for genre in fear_of_music.genres] == ["New Wave"]
    assert [album.title for album in new_wave.albums] == ["Fear of Music"]
