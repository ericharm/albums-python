from dataclasses import dataclass
from typing import Optional


@dataclass
class DatabaseConfig:
    driver: str
    database: Optional[str]
    username: Optional[str]
    password: Optional[str]
    host: Optional[str]
    port: Optional[str]
