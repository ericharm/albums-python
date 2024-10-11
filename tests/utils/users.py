from typing import Optional

from faker import Faker

from albums_python.domain.users import _encrypt_password
from albums_python.query import user_queries
from albums_python.query.models.user import User


def create_test_user(email: Optional[str] = None, password: Optional[str] = None) -> User:
    fake = Faker()

    if email is None:
        email = fake.email()

    if password is None:
        password = fake.password()

    encrypted_password = _encrypt_password(password)

    return user_queries.create_user(
        email=email,
        encrypted_password=encrypted_password,
    )
