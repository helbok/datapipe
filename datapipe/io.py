# datapipe/io.py
import os
import tempfile


def atomic_write(path, content, mode="w"):
    directory = os.path.dirname(os.path.abspath(path)) or "."
    fd, tmp = tempfile.mkstemp(dir=directory, prefix=".datapipe-", suffix=".tmp")
    try:
        with os.fdopen(fd, mode, encoding=None if "b" in mode else "utf-8") as f:
            f.write(content)
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)
    return path
