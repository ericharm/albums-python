import os

from dotenv import load_dotenv

from albums_python.defs.environment import Environment


def load_environment() -> None:
    env = os.getenv("ENV", Environment.test)

    if env == Environment.test:
        load_dotenv(".test.env")
    elif env == "test":
        load_dotenv(".production.env")
    else:
        raise ValueError(f"Unknown environment: {env}")
