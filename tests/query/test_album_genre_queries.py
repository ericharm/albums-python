from faker import Faker

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


def test_remove_album_genre_association(faker: Faker) -> None:
    rumours = album_queries.create_album(
        artist="Fleetwood Mac",
        title="Rumours",
        released="1977",
        format="LP",
        label="Warner Bros.",
        notes=None,
    )

    # Give the genres random name values to make testing easier
    rock = genre_queries.create_genre(faker.word())
    soft_rock = genre_queries.create_genre(faker.word())

    rock_association = album_genre_queries.add_genre_to_album(album=rumours, genre=rock)
    album_genre_queries.add_genre_to_album(album=rumours, genre=soft_rock)

    album_genre_queries.remove_album_genre_association(rock_association)

    # Rumours is only tagged with Soft Rock
    assert [genre.name for genre in rumours.genres] == [soft_rock.name]
    assert [album.title for album in soft_rock.albums] == ["Rumours"]

    # No albums are tagged with Rock anymore
    assert [album.title for album in rock.albums] == []


def test_get_album_genre_association_by_id(faker: Faker) -> None:
    album = album_queries.create_album(
        artist="David Bowie",
        title="The Rise and Fall of Ziggy Stardust and the Spiders from Mars",
        released="1972",
        format="LP",
        label="RCA",
        notes=None,
    )

    glam_rock = genre_queries.create_genre(faker.word())
    album_genre = album_genre_queries.add_genre_to_album(album, glam_rock)

    album_genre_association = album_genre_queries.get_album_genre_association_by_id(
        album_genre_id=album_genre.id
    )

    assert album_genre_association.to_dict() == dict(
        id=album_genre.id,
        album=album.id,
        genre=glam_rock.id,
    )


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
