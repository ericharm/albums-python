from typing import Type

from albums_python.client.database import get_db_session
from albums_python.query.models.model import Model


def clear_table(table: Type[Model]):
    with get_db_session() as session:
        session.query(table).delete()
        session.commit()  # Commit the changes


def database_model_to_dict(model: Model) -> dict:
    return {column.name: getattr(model, column.name) for column in model.__table__.columns}
