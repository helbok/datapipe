import pytest

from datapipe.errors import RegistryError
from datapipe.registry import Registry


def test_register_and_get():
    r = Registry()
    r.register("x", lambda: 42)
    assert r.get("x")() == 42
    assert "x" in r


def test_duplicate_registration_raises():
    r = Registry()
    r.register("x", lambda: 1)
    with pytest.raises(RegistryError):
        r.register("x", lambda: 2)
