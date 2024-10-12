from faker import Faker
from freezegun import freeze_time

from albums_python.domain.users import _encrypt_password
from albums_python.domain.utils import current_utc_datetime
from albums_python.query import user_queries
from tests.utils.users import create_test_user


def test_create_user(
    faker: Faker,
) -> None:
    now = current_utc_datetime()
    email = faker.email()
    password = faker.password()
    encrypted_password = _encrypt_password(password)

    with freeze_time(now):
        user = user_queries.create_user(
            email=email,
            encrypted_password=encrypted_password,
        )

    assert user.to_dict() == dict(
        id=user.id,
        email=email,
        encrypted_password=encrypted_password,
        created_at=now,
        updated_at=now,
    )


def test_get_user_by_email() -> None:
    now = current_utc_datetime()

    with freeze_time(now):
        user = create_test_user()

    found_user = user_queries.get_user_by_email(user.email)

    assert found_user
    assert found_user.to_dict() == dict(
        id=user.id,
        email=user.email,
        encrypted_password=user.encrypted_password,
        created_at=now.replace(tzinfo=None),
        updated_at=now.replace(tzinfo=None),
    )
