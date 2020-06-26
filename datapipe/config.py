# datapipe/config.py
import json
import os
from typing import Any, Dict

from datapipe.errors import ConfigurationError


def load_config(path: str) -> Dict[str, Any]:
    if not os.path.exists(path):
        raise ConfigurationError(f"config file not found: {path}")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def merge_config(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    out = dict(base)
    out.update(override)
    return out
