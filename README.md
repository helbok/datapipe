# datapipe

A composable, declarative library for building data transformation pipelines
in Python. `datapipe` models an ETL flow as a directed graph of lazily
evaluated nodes, so a pipeline can be described, inspected, validated and
replayed without executing it.

## Installation

```console
$ pip install datapipe
```

Install with optional extras for specific sources and sinks:

```console
$ pip install "datapipe[csv,sql,http,parquet]"
```

## Quick start

```python
import datapipe as dp

pipe = dp.Pipeline("orders")
orders = pipe.source("orders.csv", "csv")
clean = pipe.map(orders, "drop_missing", drop=["email"])
pipe.sink(clean, "orders.parquet", "parquet")
pipe.run()
```

## Features

- **Lazy graph execution** — nothing runs until you call `run()`.
- **Pluggable steps** — register custom transforms in the step registry.
- **Schema validation** — declare schemas and validate rows on the way in.
- **Many sources and sinks** — CSV, JSON, SQL, HTTP and Parquet.
- **Parallel execution** — run independent branches on a thread pool.

## Architecture

A pipeline is a `Graph` of `Node` objects connected by name. Each `Node`
wraps a transform that maps an iterable of rows to another iterable of rows.
`Dataset` is a handle to a node's output. Sources produce rows, sinks consume
them, and everything in between is a pure transform.

```text
source -> map -> filter -> join -> sink
              \-> aggregate -> sink
```

## Development

```console
$ pip install -e ".[test]"
$ pytest
```

## Compatibility

`datapipe` supports Python 3.9 and newer.

## Documentation

- [API reference](docs/api.md)
- [User guide](docs/guide.md)

## About this project

This repository is a **synthetic educational example**: the project and its
commit history are fictional, generated to illustrate realistic software
engineering workflows. See [HISTORY.md](HISTORY.md) for the simulated timeline.
