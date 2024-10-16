# albums-python

- `poetry shell`
- `poetry install`
- `pytest`
- `run/serve`

# TODO

- Albums
    - Search albums (discrete tests)
    - Sort by any column
    - Format enum?

- Genres
    - GET /genres
    - POST /genres
    - GET genres/<genre_id> (Don't think the original app had this feature)
        - Paginated
    - POST and DELETE album_genres/<association_id>
    - Set genres at album creation

- Deployment
    - Production WSGI
    - Find a way to run it in AWS lambda
    - Disable CORS in production

- UI
    - Search (with debounce)
    - Edit album
    - Delete album
    - The Genre select input with the pills
    - Format Enum
    - Automated deploy to S3?
    - Genre page (will this be the only page besides AlbumsPage?)
