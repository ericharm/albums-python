from albums_python.query.models.genre import Genre


def create_genre(
    name: str,
) -> Genre:
    return Genre.create(
        name=name,
    )


def get_genres_by_id(genre_ids: list[int]) -> list[Genre]:
    return Genre.select().where(Genre.id.in_(genre_ids))  # type: ignore


def get_all_genres() -> list[Genre]:
    return Genre.select()
