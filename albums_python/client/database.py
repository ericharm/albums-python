from functools import lru_cache

from peewee import Database, PostgresqlDatabase, SqliteDatabase

from albums_python.defs.database_defs import (
    DB_DRIVER,
    DB_HOST,
    DB_NAME,
    DB_PASSWORD,
    DB_PORT,
    DB_USER,
    DatabaseDriver,
)


@lru_cache(maxsize=None)
def get_database_connection() -> Database:
    if DB_DRIVER == DatabaseDriver.sqlite:
        return SqliteDatabase(DB_NAME)

    if DB_DRIVER == DatabaseDriver.postgresql:
        return PostgresqlDatabase(
            DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
        )

    raise ValueError(f"Unsupported database driver: {DB_DRIVER}")
