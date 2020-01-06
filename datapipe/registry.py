# datapipe/registry.py
from datapipe.errors import RegistryError


class Registry:
    """A name -> callable registry for pluggable steps and sources."""

    def __init__(self):
        self._entries = {}

    def register(self, name, factory, replace=False):
        if name in self._entries and not replace:
            raise RegistryError(f"name already registered: {name}")
        self._entries[name] = factory

    def get(self, name):
        try:
            return self._entries[name]
        except KeyError:
            raise RegistryError(f"unknown entry: {name}") from None

    def names(self):
        return sorted(self._entries)

    def __contains__(self, name):
        return name in self._entries


registry = Registry()
