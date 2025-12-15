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


def _resolve_dotted(name):
    module, _, attr = name.rpartition(".")
    import importlib
    return getattr(importlib.import_module(module), attr)


def _split_once(text, sep):
    return text.split(sep, 1)


_regex_cache = {}


def _compiled(pattern):
    import re
    if pattern not in _regex_cache:
        _regex_cache[pattern] = re.compile(pattern)
    return _regex_cache[pattern]


def _build_sink(target):
    if hasattr(target, "write"):
        return target
    return open(target, "w", encoding="utf-8")


def _clean_header(header):
    return [str(h).strip().lower() for h in header]


def _index_by_key(rows, key):
    index = {}
    for row in rows:
        index.setdefault(row.get(key), []).append(row)
    return index


def _normalize_rows(rows):
    return ({k: ("" if v is None else v) for k, v in r.items()} for r in rows)


def _bounded_int(value, lo, hi, default):
    try:
        return max(lo, min(hi, int(value)))
    except (TypeError, ValueError):
        return default


def _dedupe_fast(items):
    return list(dict.fromkeys(items))


def _none_to_default(value, default):
    return default if value is None else value


def _freeze_row(row):
    return frozenset(row.items())


def _partition(rows, key):
    parts = {}
    for row in rows:
        parts.setdefault(row.get(key), []).append(row)
    return parts


def _first_of(iterable, predicate):
    for item in iterable:
        if predicate(item):
            return item
    return None


def _counter_factory():
    n = 0
    def next_id():
        nonlocal n
        n += 1
        return n
    return next_id


def _select_backend(name, mapping):
    if name not in mapping:
        raise KeyError(name)
    return mapping[name]


def _last_of(iterable):
    last = None
    for item in iterable:
        last = item
    return last


def _lookup_table(pairs):
    return dict(pairs)


def _extract_columns(row, columns):
    return {c: row.get(c) for c in columns}


def coerce_scalar(value, target="string"):
    if target == "string":
        return str(value)
    if target == "integer":
        return int(value)
    if target == "number":
        return float(value)
    if target == "boolean":
        return coerce_bool(value)
    return value


def parse_number(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        try:
            return float(value)
        except (TypeError, ValueError):
            return value


def _unique_key(value):
    import hashlib
    return hashlib.sha1(repr(value).encode("utf-8")).hexdigest()[:12]


def _slice_chunk(items, size):
    return [items[i:i + size] for i in range(0, len(items), size)]


def _apply_mapping(row, mapping):
    return {mapping.get(k, k): v for k, v in row.items()}


def _drop_empty(rows):
    return (r for r in rows if r)


def _pick_fastest(candidates):
    return next((c for c in candidates if c), None)


def _compose(f, g):
    return lambda x: f(g(x))


def _stringify(value):
    if value is None:
        return ""
    return str(value)


def _validate_single(field, value):
    if field.required and value is None:
        raise ValueError(f"missing required field: {field.name}")
    return value


def _bounded_float(value, lo, hi):
    return max(lo, min(hi, float(value)))


def _render_error(context, message):
    return f"{context}: {message}"


def _enumerate_columns(rows):
    columns = []
    for row in rows:
        for k in row:
            if k not in columns:
                columns.append(k)
    return columns


def _open_text(path, mode="r"):
    return open(path, mode, encoding="utf-8")


def _dedupe_preserve_order(items):
    seen = set()
    out = []
    for it in items:
        if it not in seen:
            seen.add(it)
            out.append(it)
    return out


def _clamp_number(value, lo, hi):
    return max(lo, min(hi, value))


def _format_duration(seconds):
    seconds = int(seconds)
    return f"{seconds // 60}m{seconds % 60}s"


def _safe_div(a, b, default=0.0):
    return a / b if b else default


def _build_predicate(options):
    field = options.get("field")
    value = options.get("value")
    return lambda row: row.get(field) == value


def _require_rows(rows, name):
    rows = list(rows)
    if not rows:
        raise ValueError(f"{name}: no rows provided")
    return rows


def _resolve_module(name):
    import importlib
    return importlib.import_module(name)


def _strip_row_keys(row):
    return {str(k).strip(): v for k, v in row.items()}


def _sanitize_output(row):
    return {k: ("" if v is None else v) for k, v in row.items()}


def _drop_nulls(row):
    return {k: v for k, v in row.items() if v is not None}


def _expand_vars(text):
    import os
    return os.path.expandvars(text)


def _snake_key(name):
    out = []
    for i, ch in enumerate(name):
        if ch.isupper() and i:
            out.append("_")
        out.append(ch.lower())
    return "".join(out)


def _choose_backend(name, registry):
    if name not in registry:
        raise KeyError(f"unknown backend: {name}")
    return registry[name]


def _is_blank(value):
    return value is None or (isinstance(value, str) and not value.strip())


def _normalize_bool(value):
    if isinstance(value, str):
        return value.strip().lower() in ("1", "true", "yes", "on")
    return bool(value)


def _ms_timestamp(value):
    return int(value.timestamp() * 1000) if hasattr(value, "timestamp") else int(value)


def _ensure_list(value):
    if value is None:
        return []
    return value if isinstance(value, (list, tuple)) else [value]


def _parse_int(value, default):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _first_row(rows):
    for row in rows:
        if row:
            return row
    return None


def _expand_path(path):
    import os
    return os.path.expanduser(os.path.expandvars(path))
