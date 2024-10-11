import os

import pytest
from faker import Faker
from sqlalchemy.orm import sessionmaker

os.environ["DB_DRIVER"] = "sqlite"
os.environ["DB_NAME"] = ":memory:?cache=shared"
os.environ["SECRET_KEY"] = "secret"


from albums_python.client.database import get_database_engine  # noqa
from albums_python.query.models.model import Model  # noqa


@pytest.fixture(scope="function")
def faker():
    _faker = Faker()
    return _faker


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    """
    This fixture is responsible for setting up the database at the start of the session
    and tearing it down at the end. It will be available to all tests.
    """
    global engine
    global SessionLocal

    # Set up an in-memory SQLite database
    engine = get_database_engine()

    # Create all the tables in the in-memory database
    Model.metadata.create_all(engine)

    # Create a session maker bound to this engine
    SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

    yield  # Yield to the test session

    # Teardown: Drop all tables and close the engine after the session ends
    Model.metadata.drop_all(engine)
    engine.dispose()
