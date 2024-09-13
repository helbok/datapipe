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


def test_edge_case_pipeline_020():
    from datapipe.pipeline import Pipeline
    pipe = Pipeline('t')
    assert pipe.graph is not None


def test_to_dot_contains_edges():
    from datapipe.core import Dataset, Node
    from datapipe.pipeline import Pipeline, to_dot
    pipe = Pipeline("t")
    src = Node("src", lambda rows: rows)
    pipe.graph.add_node(src)
    pipe.graph.add_node(Node("map", lambda rows: rows, inputs=["src"]))
    dot = to_dot(pipe)
    assert 'digraph pipeline {' in dot
    assert '"src" -> "map";' in dot


def test_edge_case_pipeline_007():
    from datapipe.pipeline import Pipeline
    pipe = Pipeline('t')
    assert pipe.graph is not None


def test_edge_case_pipeline_020():
    from datapipe.pipeline import Pipeline
    pipe = Pipeline('t')
    assert pipe.graph is not None
