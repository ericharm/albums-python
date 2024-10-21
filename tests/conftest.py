import os
from typing import Callable, Generator

import pytest
from faker import Faker
from flask import Flask
from flask.testing import FlaskClient

os.environ["ENV"] = "test"
os.environ["DB_DRIVER"] = "sqlite"
os.environ["DB_NAME"] = ":memory:"
os.environ["SECRET_KEY"] = "secret"

from albums_python.client.database import get_database_connection  # noqa
from albums_python.query.models import TABLES

TestClient = Callable[[], FlaskClient]


@pytest.fixture(scope="session")
def app() -> Flask:
    from albums_python.app import app as flask_app

    flask_app.config["TESTING"] = True
    return flask_app


@pytest.fixture(scope="session")
def client(app: Flask) -> Generator[TestClient, None, None]:
    yield app.test_client


@pytest.fixture(scope="session")
def faker():
    _faker = Faker()
    return _faker


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    """
    This fixture is responsible for setting up the database at the start of the session
    and tearing it down at the end. It will be available to all tests.
    """
    db = get_database_connection()
    db.connect()
    db.create_tables(TABLES)

    yield
