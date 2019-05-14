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
    raise SourceError(f"unknown source kind: {kind}")


def read_csv(location, **options):
    def _read(rows):
        with open(location, newline="",
                  encoding=options.get("encoding", "utf-8")) as f:
            reader = csv.DictReader(f)
            for row in reader:
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
