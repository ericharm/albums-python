from albums_python.client.database import get_db_session
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

    with get_db_session() as session:
        fear_of_music = session.merge(fear_of_music)
        new_wave = session.merge(new_wave)
        album_genre_queries.add_genre_to_album(fear_of_music, new_wave)

    album_genres = [genre.to_dict() for genre in fear_of_music.genres]
    assert album_genres == [dict(id=new_wave.id, name="New Wave")]
