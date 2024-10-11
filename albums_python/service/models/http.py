from dataclasses import dataclass, field
from typing import Union

from marshmallow import validate
from marshmallow_dataclass import class_schema

Response = Union[dict, tuple[dict, int]]


@dataclass
class PaginatedRequest:
    page: int = field(default=1, metadata={"validate": validate.Range(min=1)})
    page_size: int = field(default=10, metadata={"validate": validate.Range(min=1, max=100)})


PaginatedRequestSchema = class_schema(PaginatedRequest)()


@dataclass
class PaginatedResponse:
    page: int
    page_size: int
    total_pages: int
    total_count: int
