# datapipe/cache.py
import hashlib
import json
import os
import pickle
from typing import Any, Dict, Optional


class Cache:
    """A tiny content-addressed, disk-backed cache for pipeline stages."""

    def __init__(self, directory: str) -> None:
        self.directory = directory
        os.makedirs(directory, exist_ok=True)

    def _key(self, name: str, params: Dict[str, Any]) -> str:
        raw = json.dumps({"name": name, "params": params},
                         sort_keys=True, default=str)
        return hashlib.sha1(raw.encode("utf-8")).hexdigest()

    def get(self, name: str, params: Dict[str, Any]) -> Optional[Any]:
        path = os.path.join(self.directory, self._key(name, params) + ".pkl")
        if os.path.exists(path):
            with open(path, "rb") as f:
                return pickle.load(f)
        return None

    def put(self, name: str, params: Dict[str, Any], value: Any) -> str:
        path = os.path.join(self.directory, self._key(name, params) + ".pkl")
        with open(path, "wb") as f:
            pickle.dump(value, f)
        return path
