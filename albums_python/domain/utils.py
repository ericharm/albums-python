from datetime import datetime


def current_utc_datetime() -> datetime:
    return datetime.utcnow()
