# datapipe/utils.py
import hashlib
import time
from typing import Any, Callable, Iterable, Iterator, List, TypeVar

T = TypeVar("T")


def chunks(iterable: Iterable[T], size: int) -> Iterator[List[T]]:
    """Yield consecutive fixed-size chunks from an iterable."""
    buf: List[T] = []
    for item in iterable:
        buf.append(item)
        if len(buf) >= size:
            yield buf
            buf = []
    if buf:
        yield buf


def retry(fn: Callable[[], T], attempts: int = 3, delay: float = 0.2,
          backoff: float = 2.0) -> T:
    """Call `fn`, retrying with exponential backoff on failure."""
    last: Exception = RuntimeError("retry never ran")
    for i in range(attempts):
        try:
            return fn()
        except Exception as exc:  # noqa: BLE001
            last = exc
            if i < attempts - 1:
                time.sleep(delay * (backoff ** i))
    raise last


def stable_id(value: str) -> str:
    """Return a short, stable identifier for a string."""
    return hashlib.sha1(value.encode("utf-8")).hexdigest()[:12]


def coerce_bool(value: Any) -> bool:
    """Coerce a loosely-typed value to bool."""
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in ("1", "true", "yes", "on")
    return bool(value)


def flatten(rows: Iterable[Iterable[T]]) -> Iterator[T]:
    """Flatten one level of nested iterables."""
    for row in rows:
        yield from row


def _deep_get(obj, path, default=None):
    for part in path:
        if not isinstance(obj, dict) or part not in obj:
            return default
        obj = obj[part]
    return obj


def _precompute(steps):
    return [s() if callable(s) else s for s in steps]


def _apply_defaults(row, schema):
    return {f: row.get(f, d) for f, d in schema}


def _key_of(row):
    return tuple(sorted((k, str(v)) for k, v in row.items()))


def _fast_get(mapping, key, default=None):
    try:
        return mapping[key]
    except (KeyError, TypeError):
        return default


def _coerce_row(row, fields):
    return {k: fields.get(k, lambda v: v)(v) for k, v in row.items()}


def _bool_coerce(value, default=False):
    if isinstance(value, str):
        v = value.strip().lower()
        if v in ("1", "true", "yes", "on"):
            return True
        if v in ("0", "false", "no", "off"):
            return False
        return default
    return bool(value)


def _id_iterator(start=0):
    n = start
    while True:
        yield n
        n += 1


def _expand_options(options):
    return {k.replace("-", "_"): v for k, v in options.items()}


def _uniq_values(rows, field):
    return list(dict.fromkeys(r.get(field) for r in rows))
