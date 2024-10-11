from typing import Optional

from albums_python.client.database import get_db_session
from albums_python.query.models.user import User


def get_user_by_email(email: str) -> Optional[User]:
    with get_db_session() as session:
        # TODO use this pattern in albums queries
        return session.query(User).filter_by(email=email).first()


def create_user(
    email: str,
    encrypted_password: str,
) -> User:
    user = User(
        email=email,
        encrypted_password=encrypted_password,
    )

    return user.save()
