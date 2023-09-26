from doubly_linked_list import DoublyLinkedList


class Deque:
    def __init__(self, iterable=None):
        self.dll = DoublyLinkedList(iterable)

    def append(self, value):
        self.dll.push(value)

    def appendleft(self, value):
        self.dll.append(value)

    def peek(self):
        try:
            return self.dll.head.value
        except AttributeError:
            return None

    def peekleft(self):
        try:
            return self.dll.tail.value
        except AttributeError:
            return None

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
        return len(self.dll)

    def __len__(self):
        return self.dll._size
    