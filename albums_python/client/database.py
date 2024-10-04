from dataclasses import asdict

from sqlalchemy import Engine, create_engine

from albums_python.domain.models.database import DatabaseCredentials


def get_database_engine(database_credentials: DatabaseCredentials) -> Engine:
    database, username, password, host, port = asdict(database_credentials).values()
    connection_string = f"postgresql://{username}:{password}@{host}:{port}/{database}"
    return create_engine(connection_string, echo=True)
