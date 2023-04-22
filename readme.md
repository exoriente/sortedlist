# sortedlist

A simple sorted list that maintains its sortedness under all operations:

- Based on Python's built-in sort algorithm and the `bisect` standard library
- Fully type checked using `mypy --strict`
- No dependencies
- Nothing fancy
    
This library offers two classes:

### `SortedList`

This class implements most methods of Python's built-in `list`,
except those that don't make sense for sorted data.
For example: `insert()` and `append()` are replaced by an `add()` method
that uses bisect to quickly find the appropriate place in the list for the new value.

### `SortedListByKey`

This class is much the same as `SortedList` (and inherits from it).
However, during construction it accepts sorting function as `key` parameter,
used to sort the data with the help of an arbitrary callable you can supply.
