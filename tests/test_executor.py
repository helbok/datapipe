from datapipe.core import Dataset, Graph, Node, identity
from datapipe.executor import Executor


def _dataset(name):
    g = Graph()
    n = Node(name, identity)
    g.add_node(n)
    return Dataset(name, n, g)


def test_run_branches_in_parallel():
    ex = Executor(workers=2)
    results = ex.run_branches([_dataset("a"), _dataset("b")])
    assert results == [[], []]


def test_edge_case_executor_021():
    from datapipe.executor import Executor
    ex = Executor(workers=2)
    assert ex.workers == 2
