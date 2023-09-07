import io
import sys
import pytest
from linked_list import LinkedList

def test_linked_list_init():
    my_list = LinkedList([1, 2, 3])
    assert my_list._size == 3
    assert my_list.head.value == 3
    assert my_list.head.next.value == 2
    assert my_list.head.next.next.value == 1
    assert my_list.head.next.next.next == None

def test_linked_list_init_empty():
    my_list = LinkedList()
    assert my_list._size == 0
    assert my_list.head == None

def test_linked_list_push():
    my_list = LinkedList([1, 2])
    my_list.push('hello')
    assert my_list._size == 3
    assert my_list.head.value == 'hello'
    assert my_list.head.next.value == 2
    assert my_list.head.next.next.value == 1
    assert my_list.head.next.next.next == None

def test_linked_list_push_empty():
    my_list = LinkedList([1, 2])
    my_list.push('')
    assert my_list._size == 3

def test_linked_list_display_empty():
    my_list = LinkedList()
    assert my_list.display() == "()"

def test_linked_list_display():
    my_list = LinkedList([1, 2, 3, 4, 5])
    assert my_list.display() == "(5, 4, 3, 2, 1)"

def test_linked_list_pop():
     my_list = LinkedList([3, 4, 5])
     pop = my_list.pop()
     assert pop == 5
     pop = my_list.pop()
     assert pop == 4
     pop = my_list.pop()
     assert pop == 3

def test_linked_list_pop_empty():
     with pytest.raises(ValueError, match="Pop does not work on an empty list"):
        my_list = LinkedList()
        my_list.pop()

def test_linked_list_search():
    my_list = LinkedList([1, 2, 3])
    assert my_list.search(3) == my_list.head
    assert my_list.search(2) == my_list.head.next
    assert my_list.search(1) == my_list.head.next.next

def test_linked_list_search_empty():
    my_list = LinkedList([1, 2, 3, 4, 5])
    assert my_list.search(8) == None

def test_linked_list_remove_head():
    my_list = LinkedList([1, 2, 3, 4, 5])
    my_list.remove(my_list.head)
    assert my_list._size == 4

def test_linked_list_remove():
    my_list = LinkedList([1, 2, 3, 4, 5])
    my_list.remove(my_list.head.next.next)
    assert my_list.head.next.next.value == 2

def test_linked_list_remove_non_existent():
    with pytest.raises(ValueError, match="Node not found"):
        my_list = LinkedList([1, 2, 3, 4])
        my_list.remove(5)

def test_linked_list_remove_empty():
    with pytest.raises(ValueError, match="Remove does not affect empty lists"):
        my_list = LinkedList()
        my_list.remove(5)

def test_linked_list_len():
    my_list = LinkedList([1, 2, 3])
    assert len(my_list) == 3    
    my_list.pop()
    assert len(my_list) == 2
    my_list.pop()
    assert len(my_list) == 1    
    my_list.pop()
    assert len(my_list) == 0 
    my_list.push(1)
    assert len(my_list) == 1
    my_list.push(2)
    assert len(my_list) == 2
    my_list.push(3)
    assert len(my_list) == 3
    my_list.remove(my_list.head.next)
    assert len(my_list) == 2
    my_list.remove(my_list.head.next)
    assert len(my_list) == 1
    my_list.remove(my_list.head)
    assert len(my_list) == 0

def test_linked_list_str():
    my_list = LinkedList([1, 2, 3])
    assert str(my_list) == '(3, 2, 1)'

def test_linked_list_size():
    my_list = LinkedList([1, 2, 3])
    assert (my_list).size() == 3    
    my_list.pop()
    assert (my_list).size() == 2
    my_list.pop()
    assert (my_list).size() == 1    
    my_list.pop()
    assert (my_list).size() == 0 
    my_list.push(1)
    assert (my_list).size() == 1
    my_list.push(2)
    assert (my_list).size() == 2
    my_list.push(3)
    assert (my_list).size() == 3
    my_list.remove(my_list.head.next)
    assert (my_list).size() == 2
    my_list.remove(my_list.head.next)
    assert (my_list).size() == 1
    my_list.remove(my_list.head)
    assert (my_list).size() == 0

def test_linked_list_print():
    linked_list = LinkedList([1, 2, 3, 4, 5])
    output_buffer = io.StringIO()
    sys.stdout = output_buffer   
    print(linked_list)
    sys.stdout = sys.__stdout__
    captured_output = output_buffer.getvalue()
    output_buffer.close()
    assert captured_output.strip() == "(5, 4, 3, 2, 1)"