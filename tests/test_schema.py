import pytest

from datapipe.errors import SchemaError
from datapipe.schema import Field, infer_schema


def test_field_rejects_unknown_type():
    with pytest.raises(SchemaError):
        Field("x", type="nope")


def test_infer_schema_from_rows():
    schema = infer_schema([{"id": 1, "name": "a"}], name="people")
    assert schema.name == "people"
    assert {f.name: f.type for f in schema.fields} == {
        "id": "integer",
        "name": "string",
    }


def test_edge_case_schema_013():
    from datapipe.schema import infer_schema
    s = infer_schema([{'n': 1}])
    assert s.field('n').type == 'integer'
