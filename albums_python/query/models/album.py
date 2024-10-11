from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from albums_python.domain.utils import current_utc_datetime
from albums_python.query.models.model import Model


class Album(Model):
    __tablename__ = "albums"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    artist: Mapped[str] = mapped_column(String, nullable=True)
    released: Mapped[str] = mapped_column(String, nullable=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    format: Mapped[str] = mapped_column(String, nullable=True)
    label: Mapped[str] = mapped_column(String, nullable=True)
    notes: Mapped[str] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=current_utc_datetime,
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=current_utc_datetime,
        onupdate=current_utc_datetime,
        nullable=False,
    )

    def __repr__(self) -> str:
        return f"Album<(id={self.id}, artist={self.artist}, title={self.title})"
