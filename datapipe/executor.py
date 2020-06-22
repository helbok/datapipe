# datapipe/executor.py
from concurrent.futures import ThreadPoolExecutor
from typing import Callable, Iterable, Iterator, List

from datapipe.core import Dataset, Row


class Executor:
    """Run independent pipeline branches in parallel on a thread pool."""

    def __init__(self, workers: int = 4) -> None:
        self.workers = workers

    def run_branches(self, datasets: List[Dataset]) -> List[List[Row]]:
        with ThreadPoolExecutor(max_workers=self.workers) as pool:
            futures = [pool.submit(list, d.execute()) for d in datasets]
            return [f.result() for f in futures]

    def map_parallel(self, rows: Iterable[Row], fn: Callable[[Row], Row],
                     chunk_size: int = 1000) -> Iterator[Row]:
        with ThreadPoolExecutor(max_workers=self.workers) as pool:
            yield from pool.map(fn, rows, chunksize=chunk_size)
