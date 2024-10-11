from dataclasses import dataclass
from typing import Optional


# Ugh move this please
@dataclass
class DatabaseConfig:
    driver: str
    database: Optional[str]
    username: Optional[str]
    password: Optional[str]
    host: Optional[str]
    port: Optional[str]
