class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, iterable=None):
        self.front = None
        self.rear = None
        self.size_count = 0

        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def enqueue(self, value):
        new_node = Node(value)
        if self.size_count == 0:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size_count += 1

    def dequeue(self, x=None):
        if self.size_count >= 1:
            if self.size_count == 1:
                value = self.front.value
                self.front = None
                self.rear = None
                self.size_count -= 1
                return value
            value = self.front.value
            self.front = self.front.next
            self.size_count -= 1
            return value
        else:
            raise ValueError("Queue is empty. Cannot dequeue.")

    def peek(self):
        if self.size_count > 1:
            return self.front.next.value
        else:
            return None

    def __len__(self):
        return self.size_count

    def size(self):
        return self.size_count