class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.leftchild = None
        self.rightchild = None


class BinHeap:
    def __init__(self, iterable=None):
        self.top = None
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def push(self, value):
        new_node = Node(value)

        if self.top is None:
            self.top = new_node
        else:
            current = self.top
            queue = [current]

            while queue:
                current = queue.pop(0)

                if current.leftchild is None:
                    current.leftchild = new_node
                    new_node.parent = current

                    while new_node.parent and new_node.parent.value > new_node.value:
                        new_node.parent.value, new_node.value = (
                            new_node.value,
                            new_node.parent.value,
                        )
                        new_node = new_node.parent

                    break
                elif current.rightchild is None:
                    current.rightchild = new_node
                    new_node.parent = current

                    while new_node.parent and new_node.parent.value > new_node.value:
                        new_node.parent.value, new_node.value = (
                            new_node.value,
                            new_node.parent.value,
                        )
                        new_node = new_node.parent

                    break
                else:
                    queue.append(current.leftchild)
                    queue.append(current.rightchild)

    def pop(self):
        if not self.top:
            return None

        value = self.top.value

        current = self.top
        while current.leftchild or current.rightchild:
            if current.leftchild and current.rightchild:
                if current.leftchild.value <= current.rightchild.value:
                    current = current.leftchild
                else:
                    current = current.rightchild
            elif current.leftchild:
                current = current.leftchild
            else:
                current = current.rightchild

        last_node = current

        if last_node.parent:
            if last_node.parent.leftchild == last_node:
                last_node.parent.leftchild = None
            else:
                last_node.parent.rightchild = None

        self.top.value = last_node.value

        current = self.top
        while True:
            left_child = current.leftchild
            right_child = current.rightchild
            smallest = current

            if left_child and left_child.value < smallest.value:
                smallest = left_child
            if right_child and right_child.value < smallest.value:
                smallest = right_child

            if smallest != current:
                current.value, smallest.value = smallest.value, current.value
                current = smallest
            else:
                break

        return value
