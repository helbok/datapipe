# datapipe/core.py
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, Iterable, Iterator, List, Optional

from datapipe.errors import PipelineError, ValidationError

Row = Dict[str, Any]


@dataclass
class Node:
    """A single unit of work in a pipeline graph."""
    name: str
    transform: Callable[[Iterable[Row]], Iterator[Row]]
    inputs: List[str] = field(default_factory=list)

    def run(self, rows: Iterable[Row]) -> Iterator[Row]:
        yield from self.transform(rows)


@dataclass
class Dataset:
    """A lazily evaluated collection of records flowing through a graph."""
    name: str
    node: Node
    graph: "Graph" = field(repr=False)

    def execute(self) -> Iterator[Row]:
        yield from self.graph.execute_node(self.node)


class Graph:
    """A named collection of nodes with lazy, topologically-safe execution."""

    def __init__(self) -> None:
        self._nodes: Dict[str, Node] = {}

    def add_node(self, node: Node) -> None:
        if node.name in self._nodes:
            raise PipelineError(f"node already registered: {node.name}")
        self._nodes[node.name] = node

    def node(self, name: str) -> Node:
        try:
            return self._nodes[name]
        except KeyError:
            raise PipelineError(f"unknown node: {name}") from None

    def execute_node(self, node: Node) -> Iterator[Row]:
        streams: List[Iterable[Row]] = []
        for name in node.inputs:
            streams.append(self.execute_node(self.node(name)))
        if not streams:
            yield from node.run(iter(()))
            return
        yield from node.run(_merge(streams))

    def collect(self, dataset: Dataset) -> List[Row]:
        return list(dataset.execute())


def _merge(streams: List[Iterable[Row]]) -> Iterator[Row]:
    for stream in streams:
        yield from stream


def identity(rows: Iterable[Row]) -> Iterator[Row]:
    yield from rows


def validate(rows: Iterable[Row], required: Iterable[str]) -> Iterator[Row]:
    """Yield rows, raising if a required field is missing."""
    keys = set(required)
    for row in rows:
        missing = keys - set(row)
        if missing:
            raise ValidationError(f"missing required fields: {sorted(missing)}")
        yield row
