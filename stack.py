from linked_list import LinkedList

class Stack:
    def __init__(self, iterable=None):
        self._storage = LinkedList(iterable)

    def push(self, value):
        self._storage.push(value)

    def pop(self):
        try:
            return self._storage.pop()
        except ValueError as exception:
            raise ValueError("Cannot pop from an empty stack") from exception

    def __len__(self):
        return self._storage._size