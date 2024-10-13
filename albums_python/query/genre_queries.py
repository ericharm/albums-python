from albums_python.query.models.genre import Genre


def create_genre(
    name: str,
) -> Genre:
    return Genre.create(
        name=name,
    )
