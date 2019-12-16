# datapipe/schema.py
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from datapipe.errors import SchemaError

SUPPORTED_TYPES = {"string", "integer", "number", "boolean", "date", "object"}


@dataclass
class Field:
    name: str
    type: str = "string"
    required: bool = False
    default: Any = None
    description: str = ""

    def __post_init__(self):
        if self.type not in SUPPORTED_TYPES:
            raise SchemaError(f"unsupported field type: {self.type}")


@dataclass
class Schema:
    name: str
    fields: List[Field]
    description: str = ""

    def field(self, name):
        for f in self.fields:
            if f.name == name:
                return f
        raise SchemaError(f"unknown field: {name}")

    def required_names(self):
        return [f.name for f in self.fields if f.required]


def infer_type(value):
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, int):
        return "integer"
    if isinstance(value, float):
        return "number"
    return "string"


def infer_schema(rows, name="inferred"):
    fields: List[Field] = []
    seen: Dict[str, str] = {}
    for row in rows:
        for key, value in row.items():
            t = infer_type(value)
            if key not in seen:
                seen[key] = t
                fields.append(Field(key, t))
    return Schema(name, fields)
