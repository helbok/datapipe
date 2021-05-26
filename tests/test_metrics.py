from datapipe.metrics import Metrics


def test_counters_and_timers():
    m = Metrics()
    m.count("rows", 5)
    with m.timer("stage"):
        pass
    snap = m.snapshot()
    assert snap["counters"]["rows"] == 5
    assert snap["timers"]["stage"][0] >= 0
