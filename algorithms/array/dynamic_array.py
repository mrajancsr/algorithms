"""Implementation of Dynamic Array using ctypes"""

import ctypes  # provides support for low level arrays
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class DynamicArray:
    n: int = field(init=False, default=0)
    capacity: int = field(init=False, default=1)
    A: ctypes.py_object = field(init=False)

    def __post_init__(self):
        self.A = self._make_array(self.capacity)

    def __len__(self):
        return self.n

    def __repr__(self):
        return f"DynamicArray({[self.A[i] for i in range(self.n)]})"

    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def __getitem__(self, k):
        if not 0 <= k < self.n:
            raise IndexError("Array Index Out of Bounds")
        return self.A[k]

    def append(self, val):
        if self.capacity == self.n:
            self._resize(2 * self.capacity)
        self.A[self.n] = val
        self.n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B
        self.capacity = c

    def pop(self, k: Optional[int] = None):
        if k is None or k == -1:
            item = self[self.n - 1]
            self.A[self.n - 1] = None
            self.n -= 1
            return item
        else:
            # move all elements on right of k one element to left
            item = self[k]
            for i in range(k, self.n - 1):
                self.A[i] = self.A[i + 1]
            self.A[self.n - 1] = None
            self.n -= 1
            return item
    
    def insert(self, k: int, val):
        # inserts a value at index k, shifting all elements to the right
        if k > self.n:
            raise IndexError("Index Out of Bounds")
        if self.n == self.capacity:
            self._resize(2 * self.capacity)
        for i in range(self.n, k, -1):
            self.A[i] = self[i - 1]
        self.A[k] = val
        self.n += 1



if __name__ == "__main__":
    # used only for testing code
    dyn_array = DynamicArray()
    values = [4, 5, 10, 15, 22]
    for k in values:
        dyn_array.append(k)

    print(dyn_array)
    dyn_array.insert(1, 22)
    dyn_array.insert(4, 10)
