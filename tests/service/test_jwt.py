from datetime import timedelta

from faker import Faker
from freezegun import freeze_time

from albums_python.domain.users import _generate_jwt
from albums_python.domain.utils import current_utc_datetime
from albums_python.service.jwt import _verify_jwt


def test_verify_jwt_expired_signature() -> None:
    now = current_utc_datetime()
    two_hours_ago = now - timedelta(hours=2)

    with freeze_time(two_hours_ago):
        token = _generate_jwt("user_id")

    assert _verify_jwt(token) is None


def test_verify_jwt_invalid_token(faker: Faker) -> None:
    random_token = str(faker.sha256())
    assert _verify_jwt(random_token) is None
