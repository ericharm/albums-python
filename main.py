from flask import Flask

from albums_python.client import ssm as ssm_client
from albums_python.domain.models.database import DatabaseCredentialsSchema
from albums_python.service.albums import albums_blueprint

app = Flask(__name__)
app.register_blueprint(albums_blueprint)


@app.get("/")
def hello() -> dict:
    credentials = ssm_client.get_albums_database_credentials()
    return DatabaseCredentialsSchema.dump(credentials)


if __name__ == "__main__":
    app.run()
