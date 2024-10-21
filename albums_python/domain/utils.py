from datetime import datetime
from typing import Optional, cast

from peewee import CharField, IntegerField


def current_utc_datetime() -> datetime:
    return datetime.utcnow()


def int_field_to_int(value: IntegerField) -> int:
    return cast(int, value)


def char_field_to_str(value: CharField) -> Optional[str]:
    if value is None:
        return None
    return f"{value}"
