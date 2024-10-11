from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from albums_python.domain.utils import current_utc_datetime
from albums_python.query.models.model import Model


class User(Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String, nullable=False)
    encrypted_password: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=current_utc_datetime, nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=current_utc_datetime, onupdate=datetime.utcnow, nullable=False
    )

    def __repr__(self) -> str:
        return f"User<(id={self.id}, email={self.email})"
