import json
import os
import tempfile

from datapipe.sources import create_source


def _tmp(name, content):
    d = tempfile.mkdtemp()
    path = os.path.join(d, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path


def test_read_csv_yields_rows():
    path = _tmp("in.csv", "id,name\n1,alice\n2,bob\n")
    src = create_source("csv", path)
    assert list(src(iter(()))) == [
        {"id": "1", "name": "alice"},
        {"id": "2", "name": "bob"},
    ]


def test_read_json_yields_list_items():
    path = _tmp("in.json", '[{"id": 1}, {"id": 2}]')
    src = create_source("json", path)
    assert list(src(iter(()))) == [{"id": 1}, {"id": 2}]


def test_create_source_knows_http():
    from datapipe.sources import create_source
    src = create_source("http", "https://example.com/api")
    assert callable(src)


def test_create_source_knows_sql():
    from datapipe.sources import create_source
    src = create_source("sql", "SELECT * FROM t")
    assert callable(src)


def test_edge_case_sources_009():
    from datapipe.sources import create_source
    src = create_source('memory', None, rows=[{'a': 1}])
    assert list(src(iter(()))) == [{'a': 1}]


def test_edge_case_sources_026():
    from datapipe.sources import create_source
    src = create_source('memory', None, rows=[{'a': 1}])
    assert list(src(iter(()))) == [{'a': 1}]
