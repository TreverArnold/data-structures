from linked_list import LinkedList

class Stack:
    def __init__(self, iterable=None):
        self._storage = LinkedList(iterable)

    def push(self, value):
        self._storage.push(value)

    def pop(self):
        return self._storage.pop()

    def size(self):
        return len(self._storage)

    def __len__(self):
        return self.size()