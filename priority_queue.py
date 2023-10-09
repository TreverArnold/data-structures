from binheap import BinHeap
from doubly_linked_list import DoublyLinkedList


class PriorityQueue:
    def __init__(self, iterable=None):
        self._storage = BinHeap()
        self._priority_values = {}
        if iterable is not None:
            for item in iterable:
                if (
                    not isinstance(item, int)
                    and not isinstance(item, str)
                    and len(item) == 2
                    and isinstance(item[1], int)
                ):
                    value = item[0]
                    priority = item[1]
                    self.insert(value, priority)
                else:
                    value = item
                    self.insert(value, 0)

    def insert(self, value=None, priority=None):
        if priority == None:
            priority = 0
        if priority in self._priority_values:
            self._priority_values[priority].append(value)
            self._storage.push(priority)
        else:
            self._priority_values[priority] = DoublyLinkedList([value])
            self._storage.push(priority)

    def pop(self):
        try:
            priority = self._storage.pop()
            values = self._priority_values[priority]
            value = values.pop()
            if not values:
                del self._priority_values[priority]
            return value
        except KeyError:
            raise ValueError("Cannot pop from an empty priority queue")

    def peek(self):
        if self._storage.top is not None:
            priority = self._storage.top.value
            if priority in self._priority_values:
                return self._priority_values[priority].head.value
        return None
