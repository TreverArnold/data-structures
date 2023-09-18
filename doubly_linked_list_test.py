import pytest

from doubly_linked_list import DoublyLinkedList


def test_doubly_linked_list_init():
    my_list = DoublyLinkedList([1, 2, 3])
    assert my_list._size == 3
    assert my_list.head.prev == None
    assert my_list.head.next.value == 2
    assert my_list.tail.value == 1
    assert my_list.tail.next == None
    assert my_list.tail.prev.value == 2


def test_doubly_linked_list_init_empty():
    my_list = DoublyLinkedList()
    assert my_list._size == 0
    assert my_list.head == None
    assert my_list.tail == None


def test_doubly_linked_list_append():
    my_list = DoublyLinkedList([])
    assert my_list.head == None
    assert my_list.tail == None
    assert my_list._size == 0
    my_list.append(1)
    assert my_list._size == 1
    assert my_list.head.prev == None
    assert my_list.head.next == None
    assert my_list.head.value == 1
    assert my_list.tail.value == 1
    assert my_list.tail.prev == None
    assert my_list.tail.next == None
    my_list.append(2)
    assert my_list._size == 2
    assert my_list.head.prev == None
    assert my_list.head.next.next == None
    assert my_list.head.next.value == 2
    assert my_list.head.value == 1
    assert my_list.tail.value == 2
    assert my_list.tail.prev.value == 1
    assert my_list.tail.prev.prev == None
    assert my_list.tail.next == None
    my_list.append(3)
    assert my_list._size == 3
    assert my_list.head.prev == None
    assert my_list.head.next.next.next == None
    assert my_list.head.next.next.value == 3
    assert my_list.head.next.value == 2
    assert my_list.head.value == 1
    assert my_list.tail.value == 3
    assert my_list.tail.prev.value == 2
    assert my_list.tail.prev.prev.value == 1
    assert my_list.tail.prev.prev.prev == None
    assert my_list.tail.next == None


def test_doubly_linked_list_shift():
    my_list = DoublyLinkedList([1, 2, 3])
    assert my_list.shift() == 1
    assert my_list._size == 2
    assert my_list.head.prev == None
    assert my_list.head.next.next == None
    assert my_list.head.next.value == 2
    assert my_list.head.value == 3
    assert my_list.tail.value == 2
    assert my_list.tail.prev.value == 3
    assert my_list.tail.prev.prev == None
    assert my_list.tail.next == None
    assert my_list.shift() == 2
    assert my_list._size == 1
    assert my_list.head.prev == None
    assert my_list.head.next == None
    assert my_list.head.value == 3
    assert my_list.tail.value == 3
    assert my_list.tail.prev == None
    assert my_list.tail.next == None
    assert my_list.shift() == 3
    assert my_list.head == None
    assert my_list.tail == None
    assert my_list._size == 0


def test_doubly_linked_list_shift_empty():
    with pytest.raises(ValueError, match="Shift does not work on an empty list"):
        my_list = DoublyLinkedList()
        my_list.shift()


def test_doubly_linked_list_push_empty():
    my_list = DoublyLinkedList([1, 2])
    my_list.push("")
    assert my_list._size == 3
    assert my_list.head.value == ""
    assert my_list.head.prev == None
    assert my_list.head.next.value == 2
    assert my_list.tail.value == 1
    assert my_list.tail.next == None
    assert my_list.tail.prev.value == 2


def test_doubly_linked_list_push():
    my_list = DoublyLinkedList([])
    assert my_list.head == None
    assert my_list.tail == None
    assert my_list._size == 0
    my_list.push("1")
    assert my_list._size == 1
    assert my_list.head.value == "1"
    assert my_list.tail.value == "1"
    assert my_list.tail.next == None
    assert my_list.head.prev == None
    assert my_list.head.next == None
    assert my_list.tail.prev == None
    my_list.push(2)
    assert my_list._size == 2
    assert my_list.head.value == 2
    assert my_list.tail.value == "1"
    assert my_list.head.next.value == "1"
    assert my_list.tail.prev.value == 2
    assert my_list.tail.next == None
    assert my_list.head.prev == None
    assert my_list.head.next.next == None
    assert my_list.tail.prev.prev == None
    my_list.push("3")
    assert my_list._size == 3
    assert my_list.head.value == "3"
    assert my_list.tail.value == "1"
    assert my_list.head.next.value == 2
    assert my_list.tail.prev.value == 2
    assert my_list.head.next.next.value == "1"
    assert my_list.tail.prev.prev.value == "3"
    assert my_list.tail.next == None
    assert my_list.head.prev == None
    assert my_list.head.next.next.next == None
    assert my_list.tail.prev.prev.prev == None


def test_doubly_linked_list_pop():
    dll = DoublyLinkedList([3, 2, 1])
    assert dll.head.prev == None
    assert dll.head.value == 1
    assert dll.head.next.value == 2
    assert dll.head.next.next.value == 3
    assert dll.head.next.next.next == None
    assert dll.tail.next == None
    assert dll.tail.value == 3
    assert dll.tail.prev.value == 2
    assert dll.tail.prev.prev.value == 1
    assert dll.tail.prev.prev.prev == None
    assert dll._size == 3

    assert dll.pop() == 1
    assert dll.head.prev == None
    assert dll.head.value == 2
    assert dll.head.next.value == 3
    assert dll.head.next.next == None
    assert dll.tail.next == None
    assert dll.tail.value == 3
    assert dll.tail.prev.value == 2
    assert dll.tail.prev.prev == None
    assert dll._size == 2

    assert dll.pop() == 2
    assert dll.head.prev == None
    assert dll.head.value == 3
    assert dll.head.next == None
    assert dll.tail.next == None
    assert dll.tail.value == 3
    assert dll.tail.prev == None
    assert dll._size == 1

    assert dll.pop() == 3
    assert dll.head == None
    assert dll.tail == None
    assert dll._size == 0


def test_doubly_linked_list_pop_empty():
    with pytest.raises(ValueError, match="Pop does not work on an empty list"):
        my_list = DoublyLinkedList()
        my_list.pop()


def test_doubly_linked_list_remove_head():
    my_list = DoublyLinkedList([1, 2, 3])
    my_list.remove(my_list.head)
    assert my_list._size == 2
    assert my_list.head.value == 2
    assert my_list.head.next.value == 1
    assert my_list.tail.prev.value == 2
    assert my_list.tail.value == 1
    assert my_list.tail.next == None
    assert my_list.head.prev == None


def test_doubly_linked_list_remove_tail():
    my_list = DoublyLinkedList([1, 2, 3])
    my_list.remove(my_list.tail)
    assert my_list._size == 2
    assert my_list.tail.value == 2
    assert my_list.head.next.value == 2
    assert my_list.tail.prev.value == 3
    assert my_list.head.value == 3
    assert my_list.tail.next == None
    assert my_list.head.prev == None


def test_doubly_linked_list_remove():
    my_list = DoublyLinkedList([1, 2, 3])
    my_list.remove(my_list.head.next.next)
    assert my_list.head.value == 3
    assert my_list.head.next.value == 2
    assert my_list.head.prev == None
    assert my_list.head.next.next == None
    assert my_list._size == 2
    assert my_list.tail.value == 2
    assert my_list.tail.prev.value == 3
    assert my_list.tail.next == None
    assert my_list.tail.prev.prev == None
    my_list.remove(my_list.head.next)
    assert my_list.head.value == 3
    assert my_list.head.prev == None
    assert my_list.head.next == None
    assert my_list._size == 1
    assert my_list.tail.value == 3
    assert my_list.tail.next == None
    assert my_list.tail.prev == None
    my_list.remove(my_list.head)
    assert my_list.head == None
    assert my_list.tail == None
    assert my_list._size == 0


def test_doubly_linked_list_remove_non_existent():
    with pytest.raises(ValueError, match="Node not found"):
        my_list = DoublyLinkedList([1, 2, 3])
        my_list.remove(4)


def test_doubly_linked_list_remove_empty():
    with pytest.raises(ValueError, match="Remove does not affect empty lists"):
        my_list = DoublyLinkedList()
        my_list.remove(1)


def test_doubly_linked_list_len():
    my_list = DoublyLinkedList([1, 2, 3])
    assert len(my_list) == 3
    my_list.pop()
    assert len(my_list) == 2
    my_list.push(3)
    assert len(my_list) == 3
    my_list.remove(my_list.head.next)
    assert len(my_list) == 2
    my_list.append(4)
    assert len(my_list) == 3
    my_list.shift()
    assert len(my_list) == 2
