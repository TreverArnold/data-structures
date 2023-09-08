class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, iterable=None):
        self.top = None
        self._size = 0

        if iterable is not None:
            for item in iterable:
                self.push(item)

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.top == None:
            raise ValueError('No value to pop')
        poped = self.top.value
        self.top = self.top.next
        self._size -= 1
        return poped
    
    def size(self):
        return self._size

    def __len__(self):
        return self.size()