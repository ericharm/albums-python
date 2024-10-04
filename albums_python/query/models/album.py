from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import DeclarativeBase


class Model(DeclarativeBase):
    pass


class Album(Model):
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True)
    artist = Column(String, nullable=True)
    released = Column(DateTime, nullable=True)
    title = Column(String, nullable=False)
    format = Column(String, nullable=True)
    label = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    notes = Column(String, nullable=True)

    def __repr__(self) -> str:
        return f"Album<(id={self.id!r}, artist={self.artist!r}, title={self.title!r})"
