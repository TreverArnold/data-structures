from doubly_linked_list import DoublyLinkedList


class Deque:
    def __init__(self, iterable=None):
        self.dll = DoublyLinkedList()
        self.dll.head = None
        self.dll.tail = None
        self.dll._size = 0

        if iterable is not None:
            for item in iterable:
                self.dll.push(item)

    def append(self, value):
        self.dll.append(value)

    def appendleft(self, value):
        self.dll.push(value)

    def peek(self):
        try:
            return self.dll.head.value
        except AttributeError:
            raise ValueError("Nothing to peek, que is empty")

    def peekleft(self):
        try:
            return self.dll.tail.value
        except AttributeError:
            raise ValueError("Nothing to peek, que is empty")

    def pop(self):
        try:
            return self.dll.pop()
        except ValueError:
            raise ValueError("Pop does not work on an empty queue")

    def popleft(self):
        try:
            return self.dll.shift()
        except ValueError:
            raise ValueError("Popleft does not work on an empty queue")

    def size(self):
        return self.dll._size

    def __len__(self):
        return self.dll._size
