from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self, iterable=None):
        self.dll = DoublyLinkedList()
        self.dll.head = None
        self.dll.tail = None
        self.dll._size = 0

        if iterable is not None:
            for item in iterable:
                self.dll.append(item)

    def enqueue(self, value):
        self.dll.append(value)

    def dequeue(self):
        try:
            return self.dll.pop()
        except ValueError:
            raise ValueError("Dequeue does not work on an empty queue")

    def peek(self):
        try:
            return self.dll.head.next.value
        except AttributeError:
            raise ValueError("Nothing to peek, que is either 0 or 1 item long")

    def size(self):
        return len(self.dll)

    def __len__(self):
        return len(self.dll)
