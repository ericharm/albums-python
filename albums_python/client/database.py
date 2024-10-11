from contextlib import contextmanager
from dataclasses import asdict
from functools import lru_cache
from typing import Generator

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session

from albums_python.defs.database_defs import (
    CONNECTION_STRING_FROM_DB_DRIVER,
    DB_DRIVER,
    DB_HOST,
    DB_NAME,
    DB_PASSWORD,
    DB_PORT,
    DB_USER,
)
from albums_python.domain.models.database import DatabaseConfig


@contextmanager
def get_db_session() -> Generator[Session, None, None]:
    with Session(get_database_engine(), expire_on_commit=False) as session:
        yield session


@lru_cache(maxsize=None)
def get_database_engine() -> Engine:
    config = DatabaseConfig(
        driver=DB_DRIVER,
        database=DB_NAME,
        username=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
    )

    connection_string = _get_connection_string(config)
    return create_engine(connection_string, echo=False)


def _get_connection_string(database_config: DatabaseConfig) -> str:
    driver, database, username, password, host, port = asdict(database_config).values()

    connection_string = CONNECTION_STRING_FROM_DB_DRIVER.get(driver)

    if connection_string is None:
        raise ValueError(f"Unsupported database driver: {driver}")

    return connection_string.format(
        database=database, username=username, password=password, host=host, port=port
    )
