from functools import lru_cache

from sqlalchemy import Engine

from albums_python.client import database as database_client
from albums_python.client import ssm as ssm_client


@lru_cache(maxsize=None)
def get_database() -> Engine:
    database_credentials = ssm_client.get_albums_database_credentials()
    return database_client.get_database_engine(database_credentials)
