from flask import Flask
from flask_cors import CORS


def create_app() -> Flask:
    app = Flask(__name__)

    from albums_python.service.albums_controller import albums_blueprint
    from albums_python.service.users_controller import users_blueprint

    app.register_blueprint(albums_blueprint)
    app.register_blueprint(users_blueprint)

    CORS(app)

    return app


app = create_app()
