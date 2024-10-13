from unittest.mock import ANY, patch

from faker import Faker
from freezegun import freeze_time

from albums_python.domain.utils import current_utc_datetime
from tests.conftest import TestClient
from tests.utils.users import create_test_user


def test_register_user(faker: Faker, client: TestClient) -> None:
    email = faker.email()
    password = faker.password()

    now = current_utc_datetime()

    with freeze_time(now), patch("albums_python.domain.users._generate_jwt") as mock_generate_jwt:
        mock_jwt = faker.sha256()
        mock_generate_jwt.return_value = mock_jwt

        response = client().post("/users", json=dict(email=email, password=password))
        assert response is not None
        assert response.status_code == 201
        assert response.json == dict(
            id=ANY,
            email=email,
            token=mock_jwt,
            created_at=now.isoformat(),
            updated_at=now.isoformat(),
        )


def test_login_user(faker: Faker, client: TestClient):
    email = faker.email()
    password = faker.password()

    now = current_utc_datetime()

    with freeze_time(now):
        user = create_test_user(email=email, password=password)

    with patch("albums_python.domain.users._generate_jwt") as mock_generate_jwt:
        mock_jwt = faker.sha256()
        mock_generate_jwt.return_value = mock_jwt

        response = client().post("/users/login", json=dict(email=email, password=password))
        assert response.status_code == 200
        assert response.json == dict(
            id=user.id,
            email=user.email,
            token=mock_jwt,
            created_at=now.isoformat(),
            updated_at=now.isoformat(),
        )
