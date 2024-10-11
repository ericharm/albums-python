from flask import Flask

from albums_python.domain.environment import load_environment
from albums_python.service.albums_controller import albums_blueprint
from albums_python.service.users_controller import users_blueprint

app = Flask(__name__)
app.register_blueprint(albums_blueprint)
app.register_blueprint(users_blueprint)


load_environment()

if __name__ == "__main__":
    app.run()
