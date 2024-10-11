from functools import wraps
from typing import Any, Callable, Optional

import jwt
from flask import request

from albums_python.defs.user_defs import JWT_ALGORITHM, SECRET_KEY
from albums_python.service.models.http import Response


def jwt_required(func: Callable) -> Callable:
    @wraps(func)
    def decorated_function(*args: Any, **kwargs: Any) -> Response:
        raw_token = request.headers.get("Authorization")

        if raw_token is None:
            return dict(message="Token is missing"), 403

        if not raw_token.startswith("Bearer "):
            return dict(message="Invalid token"), 403

        token = raw_token.split("Bearer ")[1]
        user_id = _verify_jwt(token)

        if user_id is None:
            return dict(message="Invalid or expired token"), 403

        return func(user_id, *args, **kwargs)

    return decorated_function


def _verify_jwt(token: str) -> Optional[str]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return payload["user_id"]
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
