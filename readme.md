# albums-python

- `poetry shell`
- `poetry install`
- `pytest`
- `cp .env.example .env`
- Update .env.  You'll need to generate a secret key on your own and map out the DB schema for the app
- `run/serve`

# TODO

- API
    - Create a production user
    - Disable /register in production
    - index album_id on album_genres
    - Create a new genre
    - Set genres at album creation
    - GET genres/<genre_id> (Don't think the original app had this feature)
        - Paginated
    - Sort albums by any column
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
