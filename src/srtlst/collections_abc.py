from sys import version_info

if version_info >= (3, 9):
    from collections.abc import Callable, Iterable, Sequence
else:
    from typing import Callable, Iterable, Sequence

__all__ = ["Callable", "Iterable", "Sequence"]
