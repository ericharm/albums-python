from __future__ import annotations

from sqlalchemy.orm import DeclarativeBase


class Model(DeclarativeBase):
    def to_dict(self) -> dict:
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
