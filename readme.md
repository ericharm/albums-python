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
    - GET /genres
    - POST /genres
    - POST and DELETE album_genres/<association_id>

    - Set genres at album creation
    - GET genres/<genre_id> (Don't think the original app had this feature)
        - Paginated

- Deployment
    - Production WSGI
    - Find a way to run it in AWS lambda
    - Disable CORS in production
    - Automate frontend deployment to S3?

- UI
    - Auto logout on 403 response (include error toast)
        - [x] Delete album
        - [ ] Create album
        - [ ] Update album
    - The Genre select input with the pills
    - Add/remove genres from album

    - Add genres to album with creation request
    - Format Enum
    - Genre page (will this be the only page besides AlbumsPage?)
    - Search on debounce?
