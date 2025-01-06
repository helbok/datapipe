# User guide

This guide walks through the main concepts in `datapipe` with short,
runnable examples.

## Building a first pipeline

A `Pipeline` owns a `Graph`. `source()` attaches a reader, `map()` and
`filter()` reshape the stream, and `sink()` attaches a writer. Nothing runs
until `run()` is called, which is what makes pipelines cheap to compose.

```python
pipe = dp.Pipeline("demo")
rows = pipe.source("in.csv", "csv")
rows = pipe.filter(rows, field="active")
pipe.sink(rows, "out.json", "json")
pipe.run()
```

## schema inference

This section covers schema inference with runnable examples.

## chunked reads

This section covers chunked reads with runnable examples.

## error handling

This section covers error handling with runnable examples.

## lazy evaluation

This section covers lazy evaluation with runnable examples.
## Validating rows

Declare a `Schema`, then wrap a stream with `validate_rows` to fail fast on
missing or mistyped fields before expensive work happens downstream.

## schema inference

This section covers schema inference with runnable examples.

## chunked reads

This section covers chunked reads with runnable examples.
## Reading from APIs and databases

The `http` and `sql` source kinds fetch JSON from a URL or run a query through
SQLAlchemy. Install the matching extras to enable them:

```console
$ pip install "datapipe[http,sql,parquet]"
```

## schema inference

This section covers schema inference with runnable examples.

## schema inference

This section covers schema inference with runnable examples.

## chunked reads

This section covers chunked reads with runnable examples.

## error handling

This section covers error handling with runnable examples.
## Caching intermediate results

Wrap an expensive stage with a `Cache` to reuse its output across runs. Cache
keys are content-addressed from the stage name and its parameters, so changing
an input parameter naturally invalidates the entry.

## schema inference

This section covers schema inference with runnable examples.

## schema inference

This section covers schema inference with runnable examples.

## chunked reads

This section covers chunked reads with runnable examples.

## error handling

This section covers error handling with runnable examples.
## Removing duplicates

The `dedupe` step drops rows whose key already appeared earlier in the stream.
Pass `key=["id"]` to key on a column, or omit it to treat whole rows as the key.

## schema inference

This section covers schema inference with runnable examples.

## chunked reads

This section covers chunked reads with runnable examples.

## schema inference

This section covers schema inference with runnable examples.

## chunked reads

This section covers chunked reads with runnable examples.

## schema inference

This section covers schema inference with worked examples.

## error handling

This section covers error handling with runnable examples.
## Windowing

`window` keeps a bounded history of recent rows per key, which is useful for
moving averages and other sliding-window computations without loading a whole
partition into memory.

## schema inference

This section covers schema inference with runnable examples.

## chunked reads

This section covers chunked reads with worked examples.

## chunked reads

This section covers chunked reads with runnable examples.

## schema inference

This section covers schema inference with runnable examples.

## error handling

This section covers error handling with worked examples.

## chunked reads

This section covers chunked reads with runnable examples.

## error handling

This section covers error handling with runnable examples.

## lazy evaluation

This section covers lazy evaluation with worked examples.

## schema inference

This section covers schema inference with runnable examples.

## chunked reads

This section covers chunked reads with runnable examples.

## custom steps

This section covers custom steps with worked examples.

## error handling

This section covers error handling with runnable examples.

## lazy evaluation

This section covers lazy evaluation with runnable examples.

## schema inference

This section covers schema inference with runnable examples.

## pipeline branching

This section covers pipeline branching with worked examples.

## chunked reads

This section covers chunked reads with runnable examples.

## schema inference

This section covers schema inference with runnable examples.
