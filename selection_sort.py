#!/usr/bin/env python3


def selection_sort(seq):
    """Returns a tuple if got a tuple. Otherwise returns a list.

    >>> t = (3, 1, 1, 4, -1, 6, 2, 9, 8, 2)
    >>> selection_sort(t)
    (-1, 1, 1, 2, 2, 3, 4, 6, 8, 9)
    >>> l = [9, 9, 3, -1, 14, 67, 1]
    >>> selection_sort(l)
    [-1, 1, 3, 9, 9, 14, 67]
    """
    alist = list(seq)
    for idx, i in enumerate(alist):
        minvalue_idx = idx
        minvalue = i
        for idx2, y in enumerate(alist[idx:]):
            if y < minvalue:
                minvalue_idx = idx + idx2
                minvalue = y
        alist[idx] = alist[minvalue_idx]
        alist[minvalue_idx] = i

    if isinstance(seq, tuple):
        return tuple(alist)

    return alist


if __name__ == "__main__":
    import doctest
    doctest.testmod()
