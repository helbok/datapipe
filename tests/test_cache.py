from datapipe.cache import Cache


def test_cache_roundtrip(tmp_path):
    cache = Cache(str(tmp_path))
    assert cache.get("stage", {"k": 1}) is None
    cache.put("stage", {"k": 1}, [1, 2, 3])
    assert cache.get("stage", {"k": 1}) == [1, 2, 3]


def test_cache_key_is_param_sensitive(tmp_path):
    cache = Cache(str(tmp_path))
    cache.put("stage", {"k": 1}, "one")
    assert cache.get("stage", {"k": 2}) is None


def test_edge_case_cache_025():
    from datapipe.cache import Cache
    import tempfile
    d = tempfile.mkdtemp()
    c = Cache(d)
    assert c.get('s', {}) is None
