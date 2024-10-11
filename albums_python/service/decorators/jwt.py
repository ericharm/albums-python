from functools import wraps
from typing import Any, Callable

from flask import jsonify, request

from albums_python.domain.users import verify_jwt


def jwt_required(func: Callable) -> Callable:
    @wraps(func)
    def decorated_function(*args: Any, **kwargs: Any):
        raw_token = request.headers.get("Authorization")
        if raw_token is None:
            return jsonify(dict(message="Token is missing")), 403

        if not raw_token.startswith("Bearer "):
            return jsonify(dict(message="Invalid token")), 403

        token = raw_token.split("Bearer ")[1]
        user_id = verify_jwt(token)
        if user_id is None:
            return jsonify(dict(message="Invalid or expired token")), 403

        return func(user_id, *args, **kwargs)

    return decorated_function
