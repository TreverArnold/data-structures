from linked_list import LinkedList

class Stack:
    def __init__(self, iterable=None):
        self._storage = LinkedList(iterable)

    def push(self, value):
        self._storage.push(value)

    def pop(self):
        try:
            return self._storage.pop()
        except ValueError:
            raise ValueError("Cannot pop from an empty stack")

    def __len__(self):
        return len(self._storage)