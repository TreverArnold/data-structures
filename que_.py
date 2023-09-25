from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self, iterable=None):
        self.dll = DoublyLinkedList()
        self.dll.head = None
        self.dll.tail = None
        self.dll._size = 0

        if iterable is not None:
            for item in iterable:
                self.dll.push(item)

    def enqueue(self, value):
        self.dll.push(value)

    def dequeue(self):
        try:
            return self.dll.shift()
        except ValueError:
            raise ValueError("Dequeue does not work on an empty queue")

    def peek(self):
        try:
            return self.dll.tail.value
        except AttributeError:
            raise ValueError("Nothing to peek, que is empty")

    def size(self):
        return len(self.dll)

    def __len__(self):
        return len(self.dll)
