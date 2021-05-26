# datapipe/metrics.py
import time
from collections import defaultdict
from contextlib import contextmanager
from typing import Any, Dict, List


class Metrics:
    """Lightweight counters and timers for pipeline observability."""

    def __init__(self) -> None:
        self.counters: Dict[str, int] = defaultdict(int)
        self.timers: Dict[str, List[float]] = defaultdict(list)

    def count(self, name: str, n: int = 1) -> None:
        self.counters[name] += n

    @contextmanager
    def timer(self, name: str):
        start = time.perf_counter()
        try:
            yield
        finally:
            self.timers[name].append(time.perf_counter() - start)

    def snapshot(self) -> Dict[str, Any]:
        return {
            "counters": dict(self.counters),
            "timers": {k: sum(v) for k, v in self.timers.items()},
        }


metrics = Metrics()
