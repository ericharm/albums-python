from datetime import datetime, timedelta
from typing import Optional, cast

import jwt
from passlib.hash import bcrypt

from albums_python.defs.user_defs import JWT_ALGORITHM, SECRET_KEY
from albums_python.domain.utils import current_utc_datetime
from albums_python.query.user_queries import create_user, get_user_by_email
from albums_python.service.models.user_schemas import UserResponse


def login_user(email: str, password: str) -> Optional[UserResponse]:
    user = get_user_by_email(email=email)

    if user and _verify_password(
        password=password, encrypted_password=f"{user.encrypted_password}"
    ):
        token, expiration = _generate_jwt(str(user.id))
        return UserResponse(
            id=cast(int, user.id),
            email=f"{user.email}",
            token=token,
            token_expiration=expiration,
            created_at=cast(datetime, user.created_at),
            updated_at=cast(datetime, user.updated_at),
        )

    return None


def register_user(email: str, password: str) -> Optional[UserResponse]:
    if get_user_by_email(email=email) is not None:
        return None

    user = create_user(email=email, encrypted_password=_encrypt_password(password))
    token, expiration = _generate_jwt(str(user.id))
    return UserResponse(
        id=cast(int, user.id),
        email=f"{user.email}",
        token=token,
        token_expiration=expiration,
        created_at=cast(datetime, user.created_at),
        updated_at=cast(datetime, user.updated_at),
    )


def _generate_jwt(user_id: str) -> tuple[str, datetime]:
    expiration = current_utc_datetime() + timedelta(hours=1)
    payload = dict(
        user_id=user_id,
        exp=expiration,
    )
    return jwt.encode(payload, SECRET_KEY, algorithm=JWT_ALGORITHM), expiration


def _encrypt_password(password: str) -> str:
    return bcrypt.hash(password)


def _verify_password(password: str, encrypted_password: str) -> bool:
    return bcrypt.verify(password, encrypted_password)
