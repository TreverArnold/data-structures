from linked_list import LinkedList

class Stack(LinkedList):
    def __init__(self, iterable=None):
        self.top = None
        self.head = None
        self._size = 0

        if iterable is not None:
            for item in iterable:
                self.push(item)

    def push(self, value):
        super().push(value)
        self.top = self.head

    def pop(self):
        popped = super().pop()
        self.top = self.head
        return popped