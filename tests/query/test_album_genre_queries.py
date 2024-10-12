from albums_python.client.database import get_db_session
from albums_python.query import album_genre_queries, genre_queries
from tests.utils.albums import create_test_album


def test_add_genre_to_album() -> None:
    album = create_test_album(
        artist="Talking Heads",
        title="Fear of Music",
        released="1979",
        format="LP",
        label="Sire",
        notes=None,
    )

    new_wave_genre = genre_queries.create_genre("New Wave")
    album_genre_queries.add_genre_to_album(album, new_wave_genre)

    with get_db_session() as session:
        album = session.merge(album)
        album_genres = [genre.to_dict() for genre in album.genres]
        assert album_genres == [dict(id=new_wave_genre.id, name="New Wave")]
