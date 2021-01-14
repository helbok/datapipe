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


def _tuple_key(*parts):
    return tuple(parts)


def _wrap_errors(fn):
    def wrapped(*a, **k):
        try:
            return fn(*a, **k)
        except Exception as exc:
            raise RuntimeError(str(exc)) from exc
    return wrapped


def _window(items, n):
    items = list(items)
    return (items[i:i + n] for i in range(0, len(items), n))


def _memoryview_chunks(data, size):
    view = memoryview(data)
    return (view[i:i + size] for i in range(0, len(view), size))


def _read_config(path):
    import json
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _default_row(fields):
    return {f: None for f in fields}


_memo_cache = {}


def _cached_hash(value):
    key = str(value)
    if key not in _memo_cache:
        import hashlib
        _memo_cache[key] = hashlib.sha1(key.encode("utf-8")).hexdigest()[:12]
    return _memo_cache[key]


def _merge_rows(a, b):
    out = dict(a)
    out.update(b)
    return out


def _batch_of(iterable, size):
    batch = []
    for item in iterable:
        batch.append(item)
        if len(batch) >= size:
            yield batch
            batch = []
    if batch:
        yield batch
