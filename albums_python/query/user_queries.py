from typing import Optional

from sqlalchemy.orm import Session

from albums_python.client.database import get_db_session
from albums_python.query.models.user import User
from albums_python.query.session import use_session


def get_user_by_email(email: str) -> Optional[User]:
    with get_db_session() as session:
        return session.query(User).filter_by(email=email).first()


@use_session
def create_user(
    email: str,
    encrypted_password: str,
    session: Optional[Session] = None,
) -> User:
    assert session
    user = User(
        email=email,
        encrypted_password=encrypted_password,
    )

    session.add(user)
    session.commit()
    return user
