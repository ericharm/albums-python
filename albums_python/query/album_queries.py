from typing import Optional, Union

from peewee import DoesNotExist

from albums_python.defs.constants import DEFAULT_NONE
from albums_python.query.models.album import Album


def get_album_by_id(album_id: int) -> Optional[Album]:
    try:
        return Album.get_by_id(album_id)
    except DoesNotExist:
        return None


def get_albums_page(page: int = 1, page_size: int = 10) -> list[Album]:
    return Album.select().order_by(Album.artist).paginate(page, page_size)


def get_albums_count() -> int:
    return Album.select().count()


def create_album(
    artist: Optional[str],
    title: str,
    released: Optional[str],
    format: Optional[str],
    label: Optional[str],
    notes: Optional[str],
) -> Album:
    return Album.create(
        artist=artist,
        title=title,
        released=released,
        format=format,
        label=label,
        notes=notes,
    )


def update_album(
    album: Album,
    artist: Union[Optional[str], object] = DEFAULT_NONE,
    title: Union[str, object] = DEFAULT_NONE,
    released: Union[Optional[str], object] = DEFAULT_NONE,
    format: Union[Optional[str], object] = DEFAULT_NONE,
    label: Union[Optional[str], object] = DEFAULT_NONE,
    notes: Union[Optional[str], object] = DEFAULT_NONE,
) -> Album:
    dirty = False
    for key, field in dict(
        artist=artist,
        title=title,
        released=released,
        format=format,
        label=label,
        notes=notes,
    ).items():
        if field != DEFAULT_NONE and getattr(album, key) != field:
            dirty = True
            setattr(album, key, field)

    if dirty:
        album.save()

    return album


def delete_album(album: Album) -> None:
    album.delete_instance()
