from collections.abc import Sequence, Callable

from pytest import fixture

from srtlst import SortedListByKey


@fixture(scope="module")
def unsortables() -> Sequence[object]:
    return [object() for _ in range(10)]


@fixture(scope="module")
def sort_function() -> Callable[[object], int]:
    return lambda x: id(x)


def test_creation_with_iterable(
    unsortables: Sequence[object], sort_function: Callable[[object], int]
) -> None:
    assert SortedListByKey(unsortables, key=sort_function) == sorted(
        unsortables, key=sort_function
    )


def test_creation_without_values(
    unsortables: Sequence[object], sort_function: Callable[[object], int]
) -> None:
    s = SortedListByKey(key=sort_function)

    for u in unsortables:
        s.add(u)

    assert s == sorted(unsortables, key=sort_function)


def test_getitem() -> None:
    s = SortedListByKey([3, 2, 1], key=lambda x: x)
    assert s[2] == 3


def test_getitem_slice() -> None:
    s = SortedListByKey([3, 2, 1], key=lambda x: x)
    result = s[1:2]
    assert isinstance(result, SortedListByKey)
    assert result == [2]


def test_copy() -> None:
    a = SortedListByKey([3, 2, 1], key=lambda x: x)
    b = a.__copy__()
    assert a == b
    assert type(b) == SortedListByKey
    assert a is not b
