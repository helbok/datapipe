from datapipe.utils import chunks, flatten, retry


def test_chunks_exact():
    assert list(chunks([1, 2, 3, 4], 2)) == [[1, 2], [3, 4]]


def test_chunks_partial():
    assert list(chunks([1, 2, 3], 2)) == [[1, 2], [3]]


def test_retry_eventually_succeeds():
    calls = []

    def flaky():
        calls.append(1)
        if len(calls) < 3:
            raise RuntimeError("boom")
        return "ok"

    assert retry(flaky, attempts=4, delay=0) == "ok"
    assert len(calls) == 3


def test_edge_case_utils_008():
    from datapipe.utils import chunks, flatten, coerce_bool
    assert list(chunks([1, 2, 3, 4], 2)) == [[1, 2], [3, 4]]
    assert list(flatten([[1], [2, 3]])) == [1, 2, 3]
    assert coerce_bool('yes') is True


def test_edge_case_utils_008():
    from datapipe.utils import chunks, flatten, coerce_bool
    assert list(chunks([1, 2, 3, 4], 2)) == [[1, 2], [3, 4]]
    assert list(flatten([[1], [2, 3]])) == [1, 2, 3]
    assert coerce_bool('yes') is True


def test_edge_case_utils_008():
    from datapipe.utils import chunks, flatten, coerce_bool
    assert list(chunks([1, 2, 3, 4], 2)) == [[1, 2], [3, 4]]
    assert list(flatten([[1], [2, 3]])) == [1, 2, 3]
    assert coerce_bool('yes') is True


def test_edge_case_utils_008():
    from datapipe.utils import chunks, flatten, coerce_bool
    assert list(chunks([1, 2, 3, 4], 2)) == [[1, 2], [3, 4]]
    assert list(flatten([[1], [2, 3]])) == [1, 2, 3]
    assert coerce_bool('yes') is True


def test_coerce_scalar():
    from datapipe.utils import coerce_scalar
    assert coerce_scalar("42", "integer") == 42
    assert coerce_scalar("1.5", "number") == 1.5


def test_parse_number_falls_back():
    from datapipe.utils import parse_number
    assert parse_number("not-a-number") == "not-a-number"


def test_edge_case_utils_008():
    from datapipe.utils import chunks, flatten, coerce_bool
    assert list(chunks([1, 2, 3, 4], 2)) == [[1, 2], [3, 4]]
    assert list(flatten([[1], [2, 3]])) == [1, 2, 3]
    assert coerce_bool('yes') is True


def test_edge_case_utils_008():
    from datapipe.utils import chunks, flatten, coerce_bool
    assert list(chunks([1, 2, 3, 4], 2)) == [[1, 2], [3, 4]]
    assert list(flatten([[1], [2, 3]])) == [1, 2, 3]
    assert coerce_bool('yes') is True


def test_edge_case_utils_003():
    from datapipe.utils import chunks, flatten, coerce_bool
    assert list(chunks([1, 2, 3, 4], 2)) == [[1, 2], [3, 4]]
    assert list(flatten([[1], [2, 3]])) == [1, 2, 3]
    assert coerce_bool('yes') is True


def test_edge_case_utils_008():
    from datapipe.utils import chunks, flatten, coerce_bool
    assert list(chunks([1, 2, 3, 4], 2)) == [[1, 2], [3, 4]]
    assert list(flatten([[1], [2, 3]])) == [1, 2, 3]
    assert coerce_bool('yes') is True


def test_edge_case_utils_008():
    from datapipe.utils import chunks, flatten, coerce_bool
    assert list(chunks([1, 2, 3, 4], 2)) == [[1, 2], [3, 4]]
    assert list(flatten([[1], [2, 3]])) == [1, 2, 3]
    assert coerce_bool('yes') is True


def test_edge_case_utils_008():
    from datapipe.utils import chunks, flatten, coerce_bool
    assert list(chunks([1, 2, 3, 4], 2)) == [[1, 2], [3, 4]]
    assert list(flatten([[1], [2, 3]])) == [1, 2, 3]
    assert coerce_bool('yes') is True


def test_edge_case_utils_008():
    from datapipe.utils import chunks, flatten, coerce_bool
    assert list(chunks([1, 2, 3, 4], 2)) == [[1, 2], [3, 4]]
    assert list(flatten([[1], [2, 3]])) == [1, 2, 3]
    assert coerce_bool('yes') is True
