import json
import os
import tempfile

from datapipe.sinks import create_sink


def test_write_json_and_read_back():
    d = tempfile.mkdtemp()
    path = os.path.join(d, "out.json")
    sink = create_sink("json", path)
    rows = [{"id": 1}, {"id": 2}]
    result = list(sink(iter(rows)))
    assert result == [{"rows_written": 2}]
    with open(path, encoding="utf-8") as f:
        assert json.load(f) == rows


def test_write_memory_collects_rows():
    buffer = []
    sink = create_sink("memory", None, buffer=buffer)
    list(sink(iter([{"a": 1}])))
    assert buffer == [{"a": 1}]


def test_create_sink_knows_parquet():
    from datapipe.sinks import create_sink
    sink = create_sink("parquet", "out.parquet")
    assert callable(sink)
