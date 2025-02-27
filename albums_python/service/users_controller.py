from flask import Blueprint
from webargs.flaskparser import use_args

from albums_python.defs.env import IS_PRODUCTION
from albums_python.domain import users as users_domain
from albums_python.service.models.http import Response
from albums_python.service.models.user_schemas import (
    LoginUserRequest,
    LoginUserRequestSchema,
    RegisterUserRequest,
    RegisterUserRequestSchema,
    UserResponseSchema,
)

users_blueprint = Blueprint("users", __name__)


@users_blueprint.post("/users")
@use_args(RegisterUserRequestSchema)
def register_user(request: RegisterUserRequest) -> Response:
    if IS_PRODUCTION:
        return dict(message="Not allowed in production"), 403

    user = users_domain.register_user(email=request.email, password=request.password)

    if user is None:
        return dict(message="Not found"), 404

    return UserResponseSchema.dump(user), 201


@users_blueprint.post("/users/login")
@use_args(LoginUserRequestSchema)
def login_user(request: LoginUserRequest) -> Response:
    user = users_domain.login_user(email=request.email, password=request.password)

    if user is None:
        return dict(message="Not found"), 404

    return UserResponseSchema.dump(user)
