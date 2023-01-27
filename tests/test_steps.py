from datapipe.steps import make_map, make_filter, make_select


def test_map_applies_fn():
    step = make_map(field="value", target="doubled", fn=lambda r: r["value"] * 2)
    rows = [{"value": 2}, {"value": 3}]
    assert list(step(iter(rows))) == [
        {"value": 2, "doubled": 4},
        {"value": 3, "doubled": 6},
    ]


def test_filter_keeps_matching():
    step = make_filter(predicate=lambda r: r["n"] > 2)
    rows = [{"n": 1}, {"n": 3}, {"n": 5}]
    assert list(step(iter(rows))) == [{"n": 3}, {"n": 5}]


def test_select_drops_columns():
    step = make_select(drop=["secret"])
    rows = [{"id": 1, "secret": "x"}, {"id": 2, "secret": "y"}]
    assert list(step(iter(rows))) == [{"id": 1}, {"id": 2}]


def test_edge_case_steps_014():
    from datapipe.steps import make_sort
    step = make_sort(key='n')
    assert list(step(iter([{'n': 2}, {'n': 1}]))) == [{'n': 1}, {'n': 2}]


def test_edge_case_steps_014():
    from datapipe.steps import make_sort
    step = make_sort(key='n')
    assert list(step(iter([{'n': 2}, {'n': 1}]))) == [{'n': 1}, {'n': 2}]


def test_edge_case_steps_014():
    from datapipe.steps import make_sort
    step = make_sort(key='n')
    assert list(step(iter([{'n': 2}, {'n': 1}]))) == [{'n': 1}, {'n': 2}]


def test_dedupe_drops_repeats():
    from datapipe.steps import make_dedupe
    step = make_dedupe(key=["id"])
    rows = [{"id": 1}, {"id": 1}, {"id": 2}]
    assert list(step(iter(rows))) == [{"id": 1}, {"id": 2}]


def test_edge_case_steps_014():
    from datapipe.steps import make_sort
    step = make_sort(key='n')
    assert list(step(iter([{'n': 2}, {'n': 1}]))) == [{'n': 1}, {'n': 2}]
