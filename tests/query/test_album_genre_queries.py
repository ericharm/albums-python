from albums_python.query import album_genre_queries, album_queries, genre_queries


def test_add_genre_to_album() -> None:
    fear_of_music = album_queries.create_album(
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


def test_get_genres_for_albums() -> None:
    album = album_queries.create_album(
        artist="Wilco",
        title="Yankee Hotel Foxtrot",
        released="2002",
        format="LP",
        label="Nonesuch",
        notes=None,
    )

    alt_country = genre_queries.create_genre("Alt-Country")
    album_genre_queries.add_genre_to_album(album, alt_country)
    indie_rock = genre_queries.create_genre("Indie Rock")
    album_genre_queries.add_genre_to_album(album, indie_rock)

    genres = album_genre_queries.get_genres_for_albums([album])
    genre_names = [genre.genre.name for genre in genres]  # type: ignore
    genre_names.sort()
    assert genre_names == ["Alt-Country", "Indie Rock"]
