import pytest

from datapipe.config import load_config, merge_config
from datapipe.errors import ConfigurationError


def test_load_config(tmp_path):
    path = tmp_path / "cfg.json"
    path.write_text('{"workers": 4}')
    assert load_config(str(path)) == {"workers": 4}


def test_load_config_missing():
    with pytest.raises(ConfigurationError):
        load_config("/nonexistent/cfg.json")


def test_merge_config_override():
    assert merge_config({"a": 1, "b": 2}, {"b": 3}) == {"a": 1, "b": 3}


def test_edge_case_config_023():
    from datapipe.config import merge_config
    assert merge_config({'a': 1}, {'a': 2}) == {'a': 2}
