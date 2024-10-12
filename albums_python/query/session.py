import functools
from typing import Any, Callable

from albums_python.client.database import get_db_session


def use_session(func: Callable) -> Callable:
    """
    A querying function will sometimes want to share a session with another querying function so
    that individual transactions can be managed together.  These functions should take a session
    parameter with the type Optional[sqlalchemy.orm.Session] and with a default value of None.
    By using this decorator, the function will check if a session was passed in. If not, it'll
    be created automatically so the caller doesn't need to pass it in.
    """

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Callable:
        session = kwargs.get("session")
        if session is None:
            with get_db_session() as session:
                kwargs["session"] = session
                return func(*args, **kwargs)
        else:
            return func(*args, **kwargs)

    return wrapper
