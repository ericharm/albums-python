# albums-python

- `poetry shell`
- `poetry install`
- `pytest`
- `run/serve`

# TODO

- Albums
    - PUT albums/<album_id>
    - DELETE albums/<album_id>
    - Search albums
    - Sort by any column
    - Format enum
    - make sure every function gets a test

- Genres
    - Set genres at album creation
    - POST and DELETE album_genres/<association_id>
    - GET genres/<genre_id>

- Deployment
    - Production WSGI
    - Find a way to run it in AWS lambda
    - Disable CORS in production

- UI
    - Search
    - Edit album
    - Delete album
    - Format Enum
