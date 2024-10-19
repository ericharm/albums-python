from dataclasses import dataclass
from datetime import datetime

from marshmallow_dataclass import class_schema


@dataclass
class RegisterUserRequest:
    email: str
    password: str


RegisterUserRequestSchema = class_schema(RegisterUserRequest)()


@dataclass
class LoginUserRequest:
    email: str
    password: str


LoginUserRequestSchema = class_schema(LoginUserRequest)()


@dataclass
class UserResponse:
    id: int
    email: str
    token: str
    token_expiration: datetime
    created_at: datetime
    updated_at: datetime


UserResponseSchema = class_schema(UserResponse)()
