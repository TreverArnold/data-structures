from binheap import BinHeap


class Node:
    def __init__(self, value=None, priority=None, insertion_order=None):
        self.value = value
        self.priority = priority
        self.insertion_order = insertion_order

    def __lt__(self, other):
        if self.priority == other.priority:
            return self.insertion_order < other.insertion_order
        return self.priority < other.priority

    def __le__(self, other):
        return self.priority <= other.priority

    def __gt__(self, other):
        if self.priority == other.priority:
            return self.insertion_order > other.insertion_order
        return self.priority > other.priority


class PriorityQueue:
    def __init__(self, iterable=None):
        self._storage = BinHeap()
        self._insertion_count = 0
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
        if priority is None:
            priority = 0
        new_node = Node(value, priority, self._insertion_count)
        self._insertion_count += 1
        self._storage.push(new_node)

    def pop(self):
        try:
            return self._storage.pop().value
        except AttributeError:
            raise ValueError("Cannot pop from an empty priority queue")

    def peek(self):
        if self._storage.top is not None:
            return self._storage.top.value.value
