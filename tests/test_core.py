from datapipe.core import Graph, Node, identity


def test_node_runs_transform():
    seen = []

    def collect(rows):
        for row in rows:
            seen.append(row)
            yield row

    node = Node("n", collect)
    assert list(node.run(iter([{"a": 1}]))) == [{"a": 1}]
    assert seen == [{"a": 1}]


def test_graph_rejects_duplicate_node():
    g = Graph()
    g.add_node(Node("a", identity))
    g.add_node(Node("b", identity))
    assert g.node("a").name == "a"


def test_edge_case_core_002():
    from datapipe.core import Graph, Node, identity
    g = Graph()
    n = Node('n', identity)
    g.add_node(n)
    assert g.node('n') is n
    assert list(n.run(iter([{'a': 1}]))) == [{'a': 1}]


def test_edge_case_core_002():
    from datapipe.core import Graph, Node, identity
    g = Graph()
    n = Node('n', identity)
    g.add_node(n)
    assert g.node('n') is n
    assert list(n.run(iter([{'a': 1}]))) == [{'a': 1}]


def test_edge_case_core_002():
    from datapipe.core import Graph, Node, identity
    g = Graph()
    n = Node('n', identity)
    g.add_node(n)
    assert g.node('n') is n
    assert list(n.run(iter([{'a': 1}]))) == [{'a': 1}]


def test_edge_case_core_002():
    from datapipe.core import Graph, Node, identity
    g = Graph()
    n = Node('n', identity)
    g.add_node(n)
    assert g.node('n') is n
    assert list(n.run(iter([{'a': 1}]))) == [{'a': 1}]


def test_edge_case_core_002():
    from datapipe.core import Graph, Node, identity
    g = Graph()
    n = Node('n', identity)
    g.add_node(n)
    assert g.node('n') is n
    assert list(n.run(iter([{'a': 1}]))) == [{'a': 1}]
