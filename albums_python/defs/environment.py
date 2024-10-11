from enum import Enum


class Environment(str, Enum):
    test = "test"
    production = "production"
