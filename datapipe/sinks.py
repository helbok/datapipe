# datapipe/sinks.py
import csv
import json
from typing import Any, Dict, Iterable, Iterator, List, Optional

from datapipe.errors import SinkError


def create_sink(kind, location, **options):
    if kind == "csv":
        return write_csv(location, **options)
    if kind == "json":
        return write_json(location, **options)
    if kind == "memory":
        return write_memory(options)
    raise SinkError(f"unknown sink kind: {kind}")


def write_csv(location, **options):
    def _write(rows):
        fieldnames = options.get("fieldnames")
        written = 0
        with open(location, "w", newline="", encoding="utf-8") as f:
            if fieldnames is None:
                first = next(rows, None)
                if first is None:
                    yield {"rows_written": 0}
                    return
                fieldnames = list(first.keys())
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow(first)
                written += 1
                for row in rows:
                    writer.writerow(row)
                    written += 1
            else:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for row in rows:
                    writer.writerow(row)
                    written += 1
        yield {"rows_written": written}
    return _write


def write_json(location, **options):
    def _write(rows):
        data = list(rows)
        with open(location, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, default=str)
        yield {"rows_written": len(data)}
    return _write


def write_memory(options):
    buffer = options.get("buffer", [])

    def _write(rows):
        for row in rows:
            buffer.append(dict(row))
        yield {"rows_written": len(buffer)}
    return _write
