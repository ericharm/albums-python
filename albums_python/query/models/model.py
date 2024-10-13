from __future__ import annotations

from peewee import Model as PeeweeModel

from albums_python.client.database import get_database_connection


class Model(PeeweeModel):
    class Meta:
        database = get_database_connection()

    def to_dict(self) -> dict:
        return self.__data__
