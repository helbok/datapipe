# datapipe/sources.py
import csv
import json
from typing import Any, Dict, Iterable, Iterator, List

from datapipe.errors import SourceError


def create_source(kind, location, **options):
    if kind == "csv":
        return read_csv(location, **options)
    if kind == "json":
        return read_json(location, **options)
    if kind == "memory":
        return read_memory(options.get("rows", []))
    if kind == "http":
        return read_http(location, **options)
    if kind == "sql":
        return read_sql(location, **options)
    raise SourceError(f"unknown source kind: {kind}")


def read_csv(location, **options):
    def _read(rows):
        with open(location, newline="",
                  encoding=options.get("encoding", "utf-8")) as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row:
                    yield row
    return _read


def read_json(location, **options):
    def _read(rows):
        with open(location, encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            for item in data:
                yield item
        else:
            yield data
    return _read


def read_memory(rows):
    def _read(_):
        for row in rows:
            yield row
    return _read


def read_http(url, **options):
    def _read(rows):
        import requests
        resp = requests.get(url, timeout=options.get("timeout", 30))
        resp.raise_for_status()
        payload = resp.json()
        if isinstance(payload, list):
            for item in payload:
                yield item
        else:
            yield payload
    return _read


def read_sql(query, **options):
    def _read(rows):
        from sqlalchemy import create_engine, text
        engine = create_engine(options["url"])
        with engine.connect() as conn:
            result = conn.execute(text(query))
            for row in result:
                yield dict(row._mapping)
    return _read
