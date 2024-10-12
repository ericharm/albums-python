from __future__ import annotations

from typing import Any

from sqlalchemy.orm import DeclarativeBase

from albums_python.client.database import get_db_session


class Model(DeclarativeBase):

    def save(self) -> Any:
        with get_db_session() as session:
            session.add(self)
            session.commit()
            return self

    def to_dict(self) -> dict:
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
