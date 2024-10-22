# albums-python

- `poetry shell`
- `poetry install`
- `pytest`
- `run/serve`

# TODO

- Albums
    - Sort by any column
    - Format enum?

- Genres
    - GET /genres (this is to fill the select options)
    - Create a new genre
    - Disable /register in production
    - index album_id on album_genres
    - Set genres at album creation
    - GET genres/<genre_id> (Don't think the original app had this feature)
        - Paginated
    - Format enum?

- UI
    - Genre pills
    - Remove genre from album
    - Genre select
    - Add genre to album
    - Auto logout on 403 response (include error toast)
        - [x] Delete album
        - [ ] Create album
        - [ ] Update album
    - Add genres to album with creation request
    - Format Enum?
    - Genre page (will this be the only page besides AlbumsPage?)
    - Search on debounce
