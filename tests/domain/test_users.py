from dataclasses import asdict
from datetime import timedelta
from unittest.mock import patch

from faker import Faker
from freezegun import freeze_time

from albums_python.domain import users as users_domain
from albums_python.domain.utils import current_utc_datetime
from tests.utils.users import create_test_user


def test_login_user(faker: Faker) -> None:
    email = faker.email()
    password = faker.password()

    now = current_utc_datetime()
    later = now + timedelta(hours=1)

    with freeze_time(now):
        user = create_test_user(email=email, password=password)

    with patch("albums_python.domain.users._generate_jwt") as mock_generate_jwt:
        mock_jwt = faker.sha256()
        mock_generate_jwt.return_value = mock_jwt, later

        user_response = users_domain.login_user(email=email, password=password)
        assert user_response is not None
        assert asdict(user_response) == dict(
            id=user.id,
            email=user.email,
            token=mock_jwt,
            token_expiration=later,
            created_at=now,
            updated_at=now,
        )


def test_login_user_incorrect_password(faker: Faker) -> None:
    email = faker.email()
    password = faker.password()
    incorrect_password = faker.password()
    create_test_user(email=email, password=password)
    user_response = users_domain.login_user(email=email, password=incorrect_password)
    assert user_response is None


def test_register_user(faker: Faker) -> None:
    email = faker.email()
    password = faker.password()

    now = current_utc_datetime()
    later = now + timedelta(hours=1)

    with (
        freeze_time(now),
        patch("albums_python.domain.users._generate_jwt") as mock_generate_jwt,
    ):
        mock_jwt = faker.sha256()
        mock_generate_jwt.return_value = mock_jwt, later

        user_response = users_domain.register_user(email=email, password=password)
        assert user_response is not None

        assert asdict(user_response) == dict(
            id=user_response.id,
            email=email,
            token=mock_jwt,
            token_expiration=later,
            created_at=now,
            updated_at=now,
        )


def test_register_user_email_already_taken(faker: Faker) -> None:
    email = faker.email()
    password = faker.password()
    create_test_user(email=email, password=password)

    user_response = users_domain.register_user(email=email, password=password)
    assert user_response is None
