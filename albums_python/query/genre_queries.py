from albums_python.query.models.genre import Genre


def create_genre(
    name: str,
) -> Genre:
    genre = Genre(
        name=name,
    )
    return genre.save()
