class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class doubly_LinkedList:
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        self._size = 0

        if iterable is not None:
            for item in iterable:
                self.push(item)

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node
        else:
            self.tail = new_node
            self.tail.prev = None

        self.head = new_node
        self.head.prev = None
        self._size += 1

        if self._size == 2:
            self.tail.next = self.head

    def append(self, value):
        new_node = Node(value)
        new_node.next = self.tail
        self.tail = new_node
        self._size += 1

        if self._size == 2:
            self.tail.next = self.head

    def display(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(repr(current.value))
            current = current.next
        return "(" + ", ".join(elements) + ")"

    def pop(self):
        if self.head is None:
            raise ValueError("Pop does not work on an empty list")

        value = self.head.value
        self.head = self.head.next
        self._size -= 1
        return value
    
    def shift(self):
        if self.tail is None:
            raise ValueError("Shift does not work on an empty list")
        value = self.tail.value
        self.tail = self.tail.prev
        self._size -= 1
        if self._size == 1:
            self.tail.next = None
            self.tail.prev = None
            self.head.next = None
            self.head.prev = None
        return value

    def search(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None

    def remove(self, node):
        if self.head is None:
            raise ValueError("Remove does not affect empty lists")

        if node == self.head:
            self.head = self.head.next
            self._size -= 1
            return

        current = self.head
        while current.next is not None:
            if current.next == node:
                current.next = current.next.next
                self._size -= 1
                return
            current = current.next

        raise ValueError("Node not found")

    def __len__(self):
        return self.size()

    def __str__(self):
        return self.display()

    def size(self):
        return self._size