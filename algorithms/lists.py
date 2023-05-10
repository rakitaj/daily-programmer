from typing import TypeVar, Self

T = TypeVar("T")


class IterableList(list[T]):
    def __init__(self):
        self.changes = 0
        self.i = 0

    def append(self, element: T):
        self.changes += 1
        super().append(element)

    def remove(self, value: T):
        self.changes += 1
        super().remove(value)

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> T:
        if self.i >= len(self):
            raise StopIteration()
        element = self[self.i]
        self.i += 1
        return element
