# API reference

## datapipe.core

- `Node` — a unit of work in a graph.
- `Dataset` — a lazy handle to a node's output.
- `Graph` — the named node collection.

## datapipe.pipeline

- `Pipeline` — builds and runs graphs.
- `to_dot` — renders a graph as Graphviz DOT.

## datapipe.schema / datapipe.validation

- `Schema`, `Field` — declarative schemas.
- `infer_schema`, `validate_rows` — schema inference and enforcement.
