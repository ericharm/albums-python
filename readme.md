# albums-python

- `poetry shell`
- `poetry install`
- `pytest`
- `run/serve`

# TODO

- Albums
    - Default albums response should be alphabetized by Artist
    - Let's make sure we're not doing n + 1 to get genres
    - PUT albums/{album_id}
    - fuzzy find across albums columns (including genres?)
    - Sort by any column
    - Delete album
    - Format enum

- Genres
    - Set genres at album creation
    - Album GET endpoints return genres
    - Get albums by genre

- Deployment
    - Production WSGI
    - Find a way to run it in AWS lambda

- UI
    - Handle API errors
    - Store the expiration of the JWT and force refresh
    - Search
    - Edit album
    - Delete album
