import functools
from typing import Any, Callable

from albums_python.client.database import get_db_session


def use_session(func: Callable) -> Callable:
    """
    A querying function will sometimes want to share a session with another querying function so
    that individual transactions can be managed together.  For any uses of these functions that do
    not need to share a session, this decorator creates a session and closes it after the function
    call.
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
