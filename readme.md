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
    - index album_id on album_genres
    - Return AlbumGenreResponse[] to AlbumResponse
    - DELETE album_genres/<association_id>
    - GET /genres (this is to fill the select options)
    - POST album_genres/<association_id>
    - POST /genres (when the genre isn't one of the listed options)
    - Disable CORS in production
    - Disable /register in production

    - Set genres at album creation
    - GET genres/<genre_id> (Don't think the original app had this feature)
        - Paginated
    - Format enum?

- UI
    - Remove genres from album
    - Add genres to album
    - Auto logout on 403 response (include error toast)
        - [x] Delete album
        - [ ] Create album
        - [ ] Update album
    - The Genre select input with the pills

    - Add genres to album with creation request
    - Format Enum?
    - Genre page (will this be the only page besides AlbumsPage?)
    - Search on debounce
