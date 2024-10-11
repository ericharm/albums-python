import os
from enum import Enum


class DatabaseDriver(str, Enum):
    postgresql = "postgresql"
    sqlite = "sqlite"


DB_DRIVER: DatabaseDriver = DatabaseDriver(os.environ["DB_DRIVER"])
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

CONNECTION_STRING_FROM_DB_DRIVER = {
    DatabaseDriver.sqlite: "sqlite:///{database}",
    DatabaseDriver.postgresql: "postgresql://{username}:{password}@{host}:{port}/{database}",
}
