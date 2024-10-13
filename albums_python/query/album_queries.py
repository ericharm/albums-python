from typing import Optional

from albums_python.query.models.album import Album


def create_album(
    artist: Optional[str],
    released: Optional[str],
    title: str,
    format: Optional[str],
    label: Optional[str],
    notes: Optional[str],
) -> Album:
    return Album.create(
        artist=artist,
        released=released,
        title=title,
        format=format,
        label=label,
        notes=notes,
    )


def get_album_by_id(album_id: int) -> Optional[Album]:
    return Album.get_by_id(album_id)


def get_albums_page(page: int = 1, page_size: int = 10) -> list[Album]:
    return Album.select().paginate(page, page_size)


def get_albums_count() -> int:
    return Album.select().count()
