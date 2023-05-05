from collections.abc import Sequence, Callable
from typing import TypeVar

from srtlst.protocols import _SupportsLT

_T = TypeVar("_T")
_S = TypeVar("_S", bound=_SupportsLT)


def bisect_left(
    seq: Sequence[_T], key_value: _S, key: Callable[[_T], _S], reverse: bool
) -> int:
    """
    return the position where an item with key_value should be inserted in
    sorted sequence seq
    if seq already contains items with a key value equal to key_value
    their first position is returned (so that the item would be inserted
    to their left)
    the function key is used to determine the key value for
    each item in the list
    if reverse is true the sequence is considered to be sorted in descending
    order
    """
    x = 0
    y = len(seq)

    if not reverse:
        while x != y:
            z = (x + y) // 2
            if key(seq[z]) < key_value:
                x = z + 1
            else:
                y = z
    else:
        while x != y:
            z = (x + y) // 2
            if key_value < key(seq[z]):
                x = z + 1
            else:
                y = z

    return x


def bisect_right(
    seq: Sequence[_T], key_value: _S, key: Callable[[_T], _S], reverse: bool
) -> int:
    """
    return the position where an item with key_value should be inserted in
    sorted sequence seq
    if seq already contains items with a key value equal to key_value
    their last position plus one is returned (so that the item would be
    inserted to their right)
    the function key is used to determine the key value for
    each item in the list
    if reverse is true the sequence is considered to be sorted in descending
    order
    """
    x = 0
    y = len(seq)

    if not reverse:
        while x != y:
            z = (x + y) // 2
            if key_value < key(seq[z]):
                y = z
            else:
                x = z + 1
    else:
        while x != y:
            z = (x + y) // 2
            if key(seq[z]) < key_value:
                y = z
            else:
                x = z + 1

    return x
