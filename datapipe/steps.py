# datapipe/steps.py
from collections import defaultdict
from typing import Any, Callable, Dict, Iterable, Iterator, List, Optional

from datapipe.core import Row
from datapipe.errors import PipelineError


def make_map(field=None, fn=None, **options):
    if fn is None and field is None:
        raise PipelineError("map requires a field or a callable")
    target = options.get("target", field)

    def _map(rows):
        for row in rows:
            out = dict(row)
            if fn is not None:
                out[target] = fn(out)
            else:
                out[target] = out.get(field)
            yield out

    return _map


def make_filter(predicate=None, field=None, **options):
    def _filter(rows):
        for row in rows:
            if predicate is not None:
                if predicate(dict(row)):
                    yield row
            elif field is not None:
                if row.get(field):
                    yield row
            else:
                yield row

    return _filter


def make_select(columns=None, drop=None, **options):
    keep = columns

    def _select(rows):
        for row in rows:
            if keep is not None:
                yield {k: row.get(k) for k in keep}
            else:
                out = dict(row)
                for k in drop or []:
                    out.pop(k, None)
                yield out

    return _select


def make_aggregate(group_by, reduce, **options):
    def _aggregate(rows):
        groups = defaultdict(list)
        for row in rows:
            key = tuple(row.get(k) for k in group_by)
            groups[key].append(dict(row))
        for key, members in groups.items():
            out = dict(zip(group_by, key))
            out.update(reduce(members))
            yield out

    return _aggregate


def make_sort(key, reverse=False, **options):
    def _sort(rows):
        buffered = list(rows)
        buffered.sort(key=lambda r: r.get(key), reverse=reverse)
        yield from buffered

    return _sort
