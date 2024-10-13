from typing import Type

from albums_python.query.models.model import Model


def clear_table(table: Type[Model]):
    table.delete().execute()
