import pytest

from datapipe.errors import ValidationError
from datapipe.schema import Field, Schema
from datapipe.validation import validate_rows


def test_validate_requires_missing_field():
    schema = Schema("s", [Field("id", required=True)])
    with pytest.raises(ValidationError):
        list(validate_rows(iter([{"nope": 1}]), schema))


def test_validate_type_mismatch():
    schema = Schema("s", [Field("id", type="integer")])
    with pytest.raises(ValidationError):
        list(validate_rows(iter([{"id": "not-an-int"}]), schema))


def test_edge_case_validation_015():
    from datapipe.schema import Field, Schema
    from datapipe.validation import validate_rows
    s = Schema('s', [Field('id', required=True)])
    assert list(validate_rows(iter([{'id': 1}]), s)) == [{'id': 1}]
