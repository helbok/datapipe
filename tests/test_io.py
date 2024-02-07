from datapipe.io import atomic_write


def test_atomic_write_creates_file(tmp_path):
    path = str(tmp_path / "out.txt")
    atomic_write(path, "hello")
    assert open(path, encoding="utf-8").read() == "hello"


def test_atomic_write_replaces_existing(tmp_path):
    path = str(tmp_path / "out.txt")
    atomic_write(path, "one")
    atomic_write(path, "two")
    assert open(path, encoding="utf-8").read() == "two"
