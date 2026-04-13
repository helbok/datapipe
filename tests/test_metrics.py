from datapipe.metrics import Metrics


def test_counters_and_timers():
    m = Metrics()
    m.count("rows", 5)
    with m.timer("stage"):
        pass
    snap = m.snapshot()
    assert snap["counters"]["rows"] == 5
    assert snap["timers"]["stage"][0] >= 0


def test_edge_case_metrics_027():
    from datapipe.metrics import Metrics
    m = Metrics()
    m.count('rows')
    assert m.snapshot()['counters']['rows'] == 1
