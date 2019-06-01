# datapipe/pipeline.py
from typing import Any, Callable, Dict, Iterable, Iterator, List, Optional

from datapipe.core import Dataset, Graph, Node, Row
from datapipe.errors import PipelineError


class Pipeline:
    """Build a data-flow graph and evaluate it lazily.

    Sources are root nodes with no inputs; sinks are terminal nodes whose
    output is discarded after the rows are written. `run()` evaluates every
    registered sink, pulling data through the graph on demand.
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self.graph = Graph()
        self._sinks: List[str] = []
        self._counter = 0

    def _register(self, transform, inputs, prefix):
        self._counter += 1
        node = Node(f"{prefix}_{self._counter}", transform, inputs)
        self.graph.add_node(node)
        return Dataset(node.name, node, self.graph)

    def source(self, location, kind="auto", **options):
        from datapipe.sources import create_source
        return self._register(create_source(kind, location, **options),
                              [], "source")

    def map(self, dataset, field=None, fn=None, **options):
        from datapipe.steps import make_map
        return self._register(make_map(field=field, fn=fn, **options),
                              [dataset.name], "map")

    def filter(self, dataset, predicate=None, field=None, **options):
        from datapipe.steps import make_filter
        return self._register(make_filter(predicate=predicate, field=field,
                                          **options), [dataset.name], "filter")

    def select(self, dataset, columns=None, drop=None, **options):
        from datapipe.steps import make_select
        return self._register(make_select(columns=columns, drop=drop, **options),
                              [dataset.name], "select")

    def aggregate(self, dataset, group_by, reduce, **options):
        from datapipe.steps import make_aggregate
        return self._register(make_aggregate(group_by, reduce, **options),
                              [dataset.name], "aggregate")

    def sort(self, dataset, key, reverse=False, **options):
        from datapipe.steps import make_sort
        return self._register(make_sort(key, reverse=reverse, **options),
                              [dataset.name], "sort")

    def sink(self, dataset, location, kind, **options):
        from datapipe.sinks import create_sink
        out = self._register(create_sink(kind, location, **options),
                             [dataset.name], "sink")
        self._sinks.append(out.name)
        return out

    def run(self):
        results = []
        for name in self._sinks:
            node = self.graph.node(name)
            results.append(self.graph.collect(Dataset(name, node, self.graph)))
        return results

    def collect(self, dataset):
        return self.graph.collect(dataset)
