from srtlst import SortedList
from pytest import raises

from srtlst.collections_abc import (
    Collection,
    Container,
    Iterable,
    Reversible,
    Sequence,
    Sized,
)


def test_creation_with_iterable() -> None:
    assert SortedList([3, 2, 1]) == [1, 2, 3]


def test_creation_with_iterable_reverse() -> None:
    assert SortedList([1, 2, 3], reverse=True) == [3, 2, 1]


def test_add() -> None:
    s: SortedList[int] = SortedList()
    s.add(3)
    s.add(1)
    s.add(2)

    assert s == [1, 2, 3]


def test_add_reverse() -> None:
    s: SortedList[int] = SortedList(reverse=True)
    s.add(3)
    s.add(1)
    s.add(2)

    assert s == [3, 2, 1]


def test_add_right() -> None:
    class Num(int):
        pass

    num1 = Num(1)
    num2 = Num(2)
    num3 = Num(3)
    num3added = Num(3)

    s = SortedList([num3, num2, num1])

    s.add_right(num3added)

    assert all(a is b for a, b in zip(s, [num1, num2, num3, num3added]))


def test_add_left() -> None:
    class Num(int):
        pass

    num1 = Num(1)
    num2 = Num(2)
    num3 = Num(3)
    num3added = Num(3)

    s = SortedList([num3, num2, num1])

    s.add_left(num3added)

    assert all(a is b for a, b in zip(s, [num1, num2, num3added, num3]))


def test_remove_right() -> None:
    class Num(int):
        pass

    num1 = Num(1)
    num2 = Num(2)
    num3 = Num(3)
    num3added = Num(3)

    s = SortedList([num3added, num3, num2, num1])

    s.remove_right(Num(3))

    assert all(a is b for a, b in zip(s, [num1, num2, num3added]))


def test_remove_left() -> None:
    class Num(int):
        pass

    num1 = Num(1)
    num2 = Num(2)
    num3 = Num(3)
    num3added = Num(3)

    s = SortedList([num3added, num3, num2, num1])

    s.remove_left(Num(3))

    assert all(a is b for a, b in zip(s, [num1, num2, num3]))


def test_remove_right_fail() -> None:
    with raises(ValueError):
        SortedList([1, 2, 3]).remove_right(4)


def test_remove_left_fail() -> None:
    with raises(ValueError):
        SortedList([1, 2, 3]).remove_left(0)


def test_repr() -> None:
    assert repr(SortedList([3, 2, 1])) == repr([1, 2, 3])


def test_pop_left() -> None:
    s = SortedList([3, 2, 1])
    assert s.pop_left() == 1
    assert s == [2, 3]


def test_pop_left_empty() -> None:
    with raises(IndexError):
        SortedList().pop_left()


def test_pop_right() -> None:
    s = SortedList([3, 2, 1])
    assert s.pop_right() == 3
    assert s == [1, 2]


def test_pop_right_empty() -> None:
    with raises(IndexError):
        SortedList().pop_right()


def test_pop() -> None:
    s = SortedList([3, 2, 1])
    assert s.pop() == 3
    assert s == [1, 2]


def test_pop_empty() -> None:
    with raises(IndexError):
        SortedList().pop()


def test_pop_with_index() -> None:
    s = SortedList([3, 2, 1])
    assert s.pop(1) == 2
    assert s == [1, 3]


def test_pop_with_index_empty() -> None:
    with raises(IndexError):
        SortedList().pop(0)


def test_extend() -> None:
    s = SortedList([3, 2, 1])
    s.extend([6, 5, 4])
    assert s == [1, 2, 3, 4, 5, 6]


def test_copy() -> None:
    a = SortedList([3, 2, 1])
    b = a.__copy__()
    assert a == b
    assert type(b) == SortedList
    assert a is not b


def test_str() -> None:
    assert str(SortedList([3, 2, 1])) == str([1, 2, 3])


def test_lt() -> None:
    assert SortedList([3, 2, 1]) < SortedList([4, 2, 1])
    assert not SortedList([3, 2, 1]) < SortedList([3, 2, 1])
    assert SortedList([3, 2, 1]) < [1, 2, 4]
    assert not SortedList([3, 2, 1]) < [1, 2, 3]


def test_le() -> None:
    assert SortedList([3, 2, 1]) <= SortedList([4, 2, 1])
    assert SortedList([3, 2, 1]) <= SortedList([3, 2, 1])
    assert SortedList([3, 2, 1]) <= [1, 2, 4]
    assert SortedList([3, 2, 1]) <= [1, 2, 3]


def test_ne() -> None:
    assert SortedList([3, 2, 1]) != [3, 2, 1]


def test_gt() -> None:
    assert SortedList([3, 2, 1]) > SortedList([2, 2, 1])
    assert not SortedList([3, 2, 1]) > SortedList([3, 2, 1])
    assert SortedList([3, 2, 1]) > [1, 2, 2]
    assert not SortedList([3, 2, 1]) > [1, 2, 3]


def test_ge() -> None:
    assert SortedList([3, 2, 1]) >= SortedList([2, 2, 1])
    assert SortedList([3, 2, 1]) >= SortedList([3, 2, 1])
    assert SortedList([3, 2, 1]) >= [1, 2, 2]
    assert SortedList([3, 2, 1]) >= [1, 2, 3]


def test_len() -> None:
    assert len(SortedList([3, 2, 1])) == 3


def test_getitem() -> None:
    s = SortedList([3, 2, 1])
    assert s[2] == 3


def test_getitem_slice() -> None:
    s = SortedList([3, 2, 1])
    result = s[1:2]
    assert isinstance(result, SortedList)
    assert result == [2]


def test_delitem() -> None:
    s = SortedList([3, 2, 1])
    del s[1]
    assert s == [1, 3]


def test_add_operator() -> None:
    assert SortedList([3, 2, 1]) + ["a", "b", "c"] == [1, 2, 3, "a", "b", "c"]


def test_mul() -> None:
    assert SortedList([3, 2, 1]) * 2 == [1, 2, 3, 1, 2, 3]


def test_contains_true() -> None:
    assert 2 in SortedList([3, 2, 1])


def test_contains_false() -> None:
    assert 4 not in SortedList([3, 2, 1])


def test_contains_bad_type() -> None:
    assert "a" not in SortedList([3, 2, 1])


def test_contains_weird_type() -> None:
    class C:
        def __eq__(self, other: object) -> bool:
            return other == 2

    assert C() in SortedList([3, 2, 1])


def test_iadd() -> None:
    s = SortedList([3, 2, 1])
    s += [6, 5, 4]
    assert s == [1, 2, 3, 4, 5, 6]


def test_reversed() -> None:
    assert list(reversed(SortedList([3, 2, 1]))) == [3, 2, 1]


def test_clear() -> None:
    s = SortedList([3, 2, 1])
    s.clear()
    assert s == []


def test_index() -> None:
    s = SortedList([3, 2, 1])
    assert s.index(3) == 2


def test_index_subsequence() -> None:
    s = SortedList([5, 4, 3, 2, 1])
    assert s.index(3, 1, 4) == 2


def test_index_error() -> None:
    s = SortedList([3, 2, 1])
    with raises(ValueError):
        s.index(4)


def test_index_subsequence_error() -> None:
    s = SortedList([5, 4, 3, 2, 1])
    with raises(ValueError):
        s.index(4, 1, 3)


def test_count() -> None:
    s = SortedList([3, 3, 3, 2, 2, 1])
    assert s.count(2) == 2


def test_is_sequence() -> None:
    assert issubclass(SortedList, Sequence)


def test_is_collection_inheritance() -> None:
    assert issubclass(SortedList, Sequence)
    assert issubclass(SortedList, Collection)
    assert issubclass(SortedList, Sized)
    assert issubclass(SortedList, Reversible)
    assert issubclass(SortedList, Iterable)
    assert issubclass(SortedList, Container)
