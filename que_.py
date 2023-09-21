from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self, iterable=None):
        self.dll = DoublyLinkedList(iterable)

    def enqueue(self, value):
        self.dll.push(value)

    def dequeue(self):
            try:
                return self.dll.shift()
            except ValueError:
                raise ValueError("Dequeue does not work on an empty queue")

    def peek(self):
        try: 
            return self.dll.tail.prev.value
        except AttributeError:
            raise AttributeError("Peek does not work on an empty queue")

    def size(self):
        return len(self.dll)
    
    def __len__(self):
        return len(self.dll)
