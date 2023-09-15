import pytest

from doubly_linked_list import doubly_LinkedList

def test_doubly_linked_list_init():
    my_list = doubly_LinkedList([1, 2, 3])
    assert my_list._size == 3
    assert my_list.head.prev == None
    assert my_list.tail.value == 1
    assert my_list.tail.next == None

def test_doubly_linked_list_init_empty():
    my_list = doubly_LinkedList()
    assert my_list._size == 0
    assert my_list.head == None
    assert my_list.tail == None

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

def test_doubly_linked_list_shift_empty():
     with pytest.raises(ValueError, match="Shift does not work on an empty list"):
        my_list = doubly_LinkedList()
        my_list.shift()

def test_doubly_linked_list_push_empty():
    my_list = doubly_LinkedList([1, 2])
    my_list.push('')
    assert my_list._size == 3
    assert my_list.head.value == ''

def test_doubly_linked_list_push():
    my_list = doubly_LinkedList([1, 2])
    my_list.push('hello')
    assert my_list._size == 3
    assert my_list.head.value == 'hello'
    assert my_list.tail.value == 1
    assert my_list.head.next.value == 2
    assert my_list.tail.prev.value == 2
    assert my_list.head.next.next.value == 1
    assert my_list.tail.prev.prev.value == 'hello'
    assert my_list.head.next.next.next == None
    assert my_list.tail.prev.prev.prev == None

def test_doubly_linked_list_pop():
     my_list = doubly_LinkedList([3, 4, 5])
     pop = my_list.pop()
     assert pop == 5
     pop = my_list.pop()
     assert pop == 4
     pop = my_list.pop()
     assert pop == 3

def test_doubly_linked_list_pop_empty():
     with pytest.raises(ValueError, match="Pop does not work on an empty list"):
        my_list = doubly_LinkedList()
        my_list.pop()

def test_doubly_linked_list_remove_head():
    my_list = doubly_LinkedList([1, 2, 3, 4, 5])
    my_list.remove(my_list.head)
    assert my_list._size == 4
    assert my_list.head.value == 4

def test_doubly_linked_list_remove_tail():
    my_list = doubly_LinkedList([1, 2, 3, 4, 5])
    my_list.remove(my_list.tail)
    assert my_list._size == 4
    assert my_list.tail.value == 2

def test_doubly_linked_list_remove():
    my_list = doubly_LinkedList([1, 2, 3, 4, 5])
    my_list.remove(my_list.head.next.next)
    assert my_list.head.next.next.value == 2

def test_doubly_linked_list_remove_non_existent():
    with pytest.raises(ValueError, match="Node not found"):
        my_list = doubly_LinkedList([1, 2, 3, 4])
        my_list.remove(5)

def test_doubly_linked_list_remove_empty():
    with pytest.raises(ValueError, match="Remove does not affect empty lists"):
        my_list = doubly_LinkedList()
        my_list.remove(5)

def test_doubly_linked_list_len():
    my_list = doubly_LinkedList([1, 2, 3])
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