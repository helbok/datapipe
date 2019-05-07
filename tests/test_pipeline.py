from datapipe.core import Dataset, Graph, Node
from datapipe.pipeline import Pipeline


def _memory_source(pipe, rows):
    def gen(_):
        yield from rows
    node = Node("src", gen)
    pipe.graph.add_node(node)
    return Dataset("src", node, pipe.graph)


def test_pipeline_map_and_collect():
    pipe = Pipeline("t")
    src = _memory_source(pipe, [{"value": 2}, {"value": 4}])
    mapped = pipe.map(src, field="value", target="double",
                      fn=lambda r: r["value"] * 2)
    assert pipe.collect(mapped) == [
        {"value": 2, "double": 4},
        {"value": 4, "double": 8},
    ]


def test_pipeline_composes_two_steps():
    pipe = Pipeline("t")
    src = _memory_source(pipe, [{"n": 1}, {"n": 5}, {"n": 3}])
    filtered = pipe.filter(src, predicate=lambda r: r["n"] > 2)
    ordered = pipe.sort(filtered, key="n")
    assert pipe.collect(ordered) == [{"n": 3}, {"n": 5}]
