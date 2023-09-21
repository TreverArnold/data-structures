from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self, iterable=None):
        self.dll = DoublyLinkedList(iterable)

    def enqueue(self, value):
        self.dll.push(value)

    def dequeue(self):
        if len(self.dll) == 0:
            raise ValueError("Dequeue does not work on an empty queue")
        return self.dll.shift()

    def peek(self):
        if len(self.dll) == 0:
            raise ValueError("Peek does not work on an empty queue")
        return self.dll.tail.prev.value

    def size(self):
        return len(self.dll)
    
    def __len__(self):
        return len(self.dll)

    def is_empty(self):
        return len(self.dll) == 0
