# datapipe/validation.py
from typing import Any, Dict, Iterable, Iterator, List, Optional

from datapipe.core import Row
from datapipe.errors import ValidationError
from datapipe.schema import Schema


def validate_rows(rows, schema):
    required = set(schema.required_names())
    for row in rows:
        missing = required - set(row)
        if missing:
            raise ValidationError(f"missing required fields: {sorted(missing)}")
        for field in schema.fields:
            if field.name in row and row[field.name] is not None:
                _check_type(row[field.name], field)
        yield row


def _check_type(value, field):
    t = field.type
    ok = True
    if t == "integer":
        ok = isinstance(value, int) and not isinstance(value, bool)
    elif t == "number":
        ok = isinstance(value, (int, float)) and not isinstance(value, bool)
    elif t == "boolean":
        ok = isinstance(value, bool)
    elif t == "string":
        ok = isinstance(value, str)
    if not ok:
        raise ValidationError(
            f"field {field.name!r} expected {t}, got {type(value).__name__}"
        )


def validate_value(value, field):
    _check_type(value, field)
    return True
