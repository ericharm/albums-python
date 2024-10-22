from flask import Flask
from flask_cors import CORS

from albums_python.defs.env import ALLOWED_HOSTS, ENV


def create_app() -> Flask:
    app = Flask(__name__)

    from albums_python.service.album_genres_controller import album_genres_blueprint
    from albums_python.service.albums_controller import albums_blueprint
    from albums_python.service.genres_controller import genres_blueprint
    from albums_python.service.users_controller import users_blueprint

    app.register_blueprint(albums_blueprint)
    app.register_blueprint(album_genres_blueprint)
    app.register_blueprint(genres_blueprint)
    app.register_blueprint(users_blueprint)

    if ENV == "local":
        CORS(app)
    else:
        CORS(app, origins=[ALLOWED_HOSTS])

    return app


app = create_app()
