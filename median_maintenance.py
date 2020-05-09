"""Python solution for median maintenance.

>>> stream = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> maintainer = MedianMaintainer()
>>> for i in range(len(stream)):
...     maintainer.append(stream[i])
...     print(maintainer.median, stream[:i+1])
...
0 [0]
0 [0, 1]
1 [0, 1, 2]
1 [0, 1, 2, 3]
2 [0, 1, 2, 3, 4]
2 [0, 1, 2, 3, 4, 5]
3 [0, 1, 2, 3, 4, 5, 6]
3 [0, 1, 2, 3, 4, 5, 6, 7]
4 [0, 1, 2, 3, 4, 5, 6, 7, 8]
4 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""


from heap import Heap


class MedianMaintainer:
    """The median is defined as ((n+1)/2)th element if n is odd and (n/2)th element if n is even."""

    def __init__(self):
        self.smaller = Heap(maxheap=True)
        self.bigger = Heap()
        self.median = float('inf')

    def _balance(self):
        if abs(len(self.smaller) - len(self.bigger)) > 1:
            if len(self.smaller) > len(self.bigger):
                self.bigger.insert_node(self.smaller.extract_root())
            else:
                self.smaller.insert_node(self.bigger.extract_root())

    def append(self, num):
        # choose where to place a new number.
        if num > self.median:
            self.bigger.insert_node(num)
        else:
            self.smaller.insert_node(num)

        # Ensure heaps length do not differ by more than one.
        self._balance()

        # set median
        self.median = self.smaller[0] if len(self.smaller) >= len(self.bigger) else self.bigger[0]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
