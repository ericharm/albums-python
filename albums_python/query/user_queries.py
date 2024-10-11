from typing import Optional

from albums_python.client.database import get_db_session
from albums_python.domain.utils import current_utc_datetime
from albums_python.query.models.user import User


def get_user_by_email(email: str) -> Optional[User]:
    with get_db_session() as session:
        return session.query(User).filter_by(email=email).first()


def create_user(
    email: str,
    encrypted_password: str,
) -> User:
    now = current_utc_datetime()
    user = User(
        email=email,
        encrypted_password=encrypted_password,
        created_at=now,
        updated_at=now,
    )

    return user.save()
