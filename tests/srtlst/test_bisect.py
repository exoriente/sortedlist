from srtlst.collections_abc import Callable

from srtlst.bisect import bisect_left, bisect_right

from pytest import fixture


@fixture
def key() -> Callable[[int], int]:
    return lambda x: x


def test_bisect_left(key: Callable[[int], int]) -> None:
    assert bisect_left([], 0, key, False) == 0
    assert bisect_left([1], 0, key, False) == 0
    assert bisect_left([0], 1, key, False) == 1
    assert bisect_left([0, 1], 2, key, False) == 2
    assert bisect_left([0, 1], 1, key, False) == 1
    assert bisect_left([0, 1], 0, key, False) == 0
    assert bisect_left([0, 0, 1, 1], 2, key, False) == 4
    assert bisect_left([0, 0, 1, 1], 1, key, False) == 2
    assert bisect_left([0, 0, 1, 1], 0, key, False) == 0


def test_bisect_left_reverse(key: Callable[[int], int]) -> None:
    assert bisect_left([], 0, key, True) == 0
    assert bisect_left([1], 0, key, True) == 1
    assert bisect_left([0], 1, key, True) == 0
    assert bisect_left([1, 0], 2, key, True) == 0
    assert bisect_left([1, 0], 1, key, True) == 0
    assert bisect_left([1, 0], 0, key, True) == 1
    assert bisect_left([1, 1, 0, 0], 2, key, True) == 0
    assert bisect_left([1, 1, 0, 0], 1, key, True) == 0
    assert bisect_left([1, 1, 0, 0], 0, key, True) == 2


def test_bisect_right(key: Callable[[int], int]) -> None:
    assert bisect_right([], 0, key, False) == 0
    assert bisect_right([1], 0, key, False) == 0
    assert bisect_right([0], 1, key, False) == 1
    assert bisect_right([0, 1], 2, key, False) == 2
    assert bisect_right([0, 1], 1, key, False) == 2
    assert bisect_right([0, 1], 0, key, False) == 1
    assert bisect_right([0, 0, 1, 1], 2, key, False) == 4
    assert bisect_right([0, 0, 1, 1], 1, key, False) == 4
    assert bisect_right([0, 0, 1, 1], 0, key, False) == 2


def test_bisect_right_reverse(key: Callable[[int], int]) -> None:
    assert bisect_right([], 0, key, True) == 0
    assert bisect_right([1], 0, key, True) == 1
    assert bisect_right([0], 1, key, True) == 0
    assert bisect_right([1, 0], 2, key, True) == 0
    assert bisect_right([1, 0], 1, key, True) == 1
    assert bisect_right([1, 0], 0, key, True) == 2
    assert bisect_right([1, 1, 0, 0], 2, key, True) == 0
    assert bisect_right([1, 1, 0, 0], 1, key, True) == 2
    assert bisect_right([1, 1, 0, 0], 0, key, True) == 4


@fixture
def alt_key() -> Callable[[int], int]:
    return lambda x: x * (-1) ** x


def test_alt_key(alt_key: Callable[[int], int]) -> None:
    assert bisect_left([3, 1, 2, 4], -1, alt_key, False) == 1
    assert bisect_right([3, 1, 2, 4], -1, alt_key, False) == 2
    assert bisect_left([4, 2, 1, 3], -1, alt_key, True) == 2
    assert bisect_right([4, 2, 1, 3], -1, alt_key, True) == 3
