# pyre-strict
"""Linear Collections, consisting of stacks, queue and deque"""

from dataclasses import dataclass, field
from typing import Any, List, Union


class Empty(Exception):
    pass


@dataclass
class Stack:
    """Implementation of Stack using Lists

    O(1) time for all operations
    O(n) time for max operation
    Assumes LIFO
    items on the right is the top, left is the bottom
    """

    data: List[int] = field(init=False, default=lambda: [])

    def __repr__(self):
        return f"Stack({self.data})"

    def empty(self) -> bool:
        """Returns True if Stack is empty, false otherwise

        Returns
        -------
        bool
            True if Stack is empty, false otherwise
        """
        return self.data == []

    def push(self, item: Any):
        """Adds an item to top (right) of stack

        Parameters
        ----------
        item : Any
            item to be pushed
        """
        self.data.append(item)

    def peek(self) -> Any:
        """Returns the last item in stack

        Returns
        -------
        Any
            Last item in the stack
        """
        return self.data[-1]

    def pop(self) -> Any:
        """removes last element from stack

        Returns
        -------
        Any
            the item thats removed

        Raises
        ------
        Empty
            if stack is empty
        """
        if self.empty():
            raise Empty("Stack is empty")
        return self.data.pop()


@dataclass
class CachedMax:
    element: int
    max: int


@dataclass
class StackWithMax:
    data: List[CachedMax] = field(
        init=False,
        default_factory=lambda: [],
    )

    def __repr__(self):
        return f"StackWithMax({self.data})"

    def empty(self):
        return self.data == []

    def pop(self):
        if self.empty():
            raise Empty("Stack is empty")
        return self.data.pop().element

    def peek(self):
        if self.empty():
            raise Empty("Stack is empty")
        return self.data[-1].element

    def max(self):
        if self.empty():
            raise Empty("Stack is empty")
        return self.data[-1].max

    def push(self, item):
        self.data.append(
            CachedMax(
                item,
                item if self.empty() else max(item, self.max()),
            )
        )


@dataclass
class CachedMaxWithCount:
    max: int
    count: int


@dataclass
class StackWithMaxCount:
    data: List[int] = field(init=False, default_factory=lambda: [])
    cached_max_with_count: List[CachedMaxWithCount] = field(
        init=False, default_factory=lambda: []
    )

    def __repr__(self):
        return (
            "data: "
            + repr(self.data)
            + "\n"
            + "cached_max_with_count: "
            + repr(self.cached_max_with_count)
        )

    def empty(self):
        return self.data == []

    def peek(self):
        return self.data[-1]

    def pop(self):
        if self.empty():
            raise Empty("Stack is empty")
        popped_element = self.data.pop()
        current_max = self.cached_max_with_count[-1].max
        if popped_element == current_max:
            self.cached_max_with_count[-1].count -= 1
            if self.cached_max_with_count[-1].count == 0:
                self.cached_max_with_count.pop()
        return popped_element

    def push(self, item):
        self.data.append(item)
        if len(self.cached_max_with_count) == 0:
            self.cached_max_with_count.append(CachedMaxWithCount(item, 1))
        else:
            current_max = self.cached_max_with_count[-1].max
            if item == current_max:
                self.cached_max_with_count[-1].count += 1
            elif item > current_max:
                self.cached_max_with_count.append(CachedMaxWithCount(item, 1))

    def max(self):
        if self.empty():
            raise Empty("Stack is empty")
        return self.cached_max_with_count[-1].max


@dataclass
class QueueWithStacks:
    enq: Stack = field(init=False)
    deq: Stack = field(init=False)

    def __post_init__(self):
        self.enq = Stack()
        self.deq = Stack()

    def enqueue(self, item):
        self.enq.push(item)

    def dequeue(self):
        if not self.deq:
            while not self.enq.empty():
                self.deq.push(self.enq.pop())
        if not self.deq:
            raise Empty("Stack is empty")
        return self.deq.pop()
