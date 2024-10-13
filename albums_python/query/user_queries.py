from typing import Optional

from peewee import DoesNotExist

from albums_python.query.models.user import User


def get_user_by_email(email: str) -> Optional[User]:
    try:
        return User.get(User.email == email)
    except DoesNotExist:
        return None


def create_user(
    email: str,
    encrypted_password: str,
) -> User:
    return User.create(
        email=email,
        encrypted_password=encrypted_password,
    )
