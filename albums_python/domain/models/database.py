from dataclasses import dataclass

from marshmallow_dataclass import class_schema


@dataclass
class DatabaseCredentials:
    database: str
    username: str
    password: str
    host: str
    port: int


DatabaseCredentialsSchema = class_schema(DatabaseCredentials)()
