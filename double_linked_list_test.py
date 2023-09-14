from doubly_linked_list import doubly_LinkedList

def test_doubly_linked_list_init():
    my_list = doubly_LinkedList([1, 2, 3])
    assert my_list._size == 3
    assert my_list.head.prev == None
    assert my_list.tail.value == 1
    assert my_list.tail.next.value == 2

def test_doubly_linked_list_append():
    my_list = doubly_LinkedList([1, 2])
    my_list.append(3)
    assert my_list.tail.value == 3
    assert my_list.tail.next.value == 1
    assert my_list._size == 3

def test_doubly_linked_list_shift():
    my_list = doubly_LinkedList([1, 2])
    assert my_list.shift() == 1
    assert my_list.tail.value == 2
    assert my_list.tail.next == None
    assert my_list._size == 1
