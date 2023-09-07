class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, iterable=None):
        self.head = None
        self._size = 0

        if iterable is not None:
            for item in iterable:
                self.push(item)

    def push(self, value):
        if value is None or (isinstance(value, str) and not value.strip()):
            raise ValueError("Push needs a value")
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def display(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(repr(current.value))
            current = current.next
        return "(" + ", ".join(elements) + ")"

    def pop(self):
        if self.head is None:
            raise ValueError("Pop does not work on empty array or list")

        value = self.head.value
        self.head = self.head.next
        self._size -= 1
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
            raise ValueError("Remove does not work on empty lists")

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
