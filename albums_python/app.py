from flask import Flask
from flask_cors import CORS


def create_app() -> Flask:
    app = Flask(__name__)

    CORS(app)

    from albums_python.service.album_genres_controller import album_genres_blueprint
    from albums_python.service.albums_controller import albums_blueprint
    from albums_python.service.genres_controller import genres_blueprint
    from albums_python.service.users_controller import users_blueprint

    app.register_blueprint(albums_blueprint)
    app.register_blueprint(album_genres_blueprint)
    app.register_blueprint(genres_blueprint)
    app.register_blueprint(users_blueprint)

    return app


app = create_app()
