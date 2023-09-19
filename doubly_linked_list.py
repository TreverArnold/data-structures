class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
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

        self.head = new_node
        self._size += 1

    def append(self, value):
        new_node = Node(value)
        new_node.prev = self.tail
        self.tail = new_node
        self._size += 1
        if self.head is not None:
            self.tail.prev.next = new_node
        else:
            self.head = new_node

    def pop(self):
        if self.head is None:
            raise ValueError("Pop does not work on an empty list")
        value = self.head.value
        self.head = self.head.next
        if self._size != 1:
            self.head.prev = None
        self._size -= 1
        if self._size == 0:
            self.tail = None
        return value

    def shift(self):
        if self.tail is None:
            raise ValueError("Shift does not work on an empty list")
        value = self.tail.value
        if self._size != 1:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            self.tail = None
            self.head = None
        self._size -= 1
        return value

    def remove(self, node):
        if self.head is None:
            raise ValueError("Remove does not affect empty lists")

        if node == self.head:
            if self._size != 1:
                self.head.next.prev = None
            self.head = self.head.next
            if node == self.tail:
                self.tail = None
            self._size -= 1
            return

        current = self.head
        while current.next is not None:
            if current.next == node:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                self._size -= 1
                return
            current = current.next

        raise ValueError("Node not found")


    def search(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None
    
    def __len__(self):
        return self._size
