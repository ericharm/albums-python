from datetime import datetime

from dateutil.tz import tz


def current_utc_datetime() -> datetime:
    return datetime.utcnow().replace(tzinfo=tz.tzutc())
