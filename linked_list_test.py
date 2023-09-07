from linked_list import LinkedList
import io
import sys
import pytest

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
    with pytest.raises(ValueError):
        my_list = LinkedList([1, 2])
        my_list.push('')
    assert my_list._size == 2

def test_linked_list_display_empty():
    my_list = LinkedList()
    assert my_list.display() == "()"

def test_linked_list_display():
    my_list = LinkedList([1, 2, 3, 4, 5])
    assert my_list.display() == "(5, 4, 3, 2, 1)"
    linked_list = LinkedList([1, 2, 3, 4, 5])
    print(linked_list)
    captured_output = capture_output_for_print_test(print)(linked_list)
    expected_output = "(5, 4, 3, 2, 1)"
    assert captured_output.strip() == expected_output

def test_linked_list_pop():
     my_list = LinkedList([3, 4, 5])
     pop1 = my_list.pop()
     pop2 = my_list.pop()
     pop3 = my_list.pop()
     pops = repr(pop1) + ", " + repr(pop2) + ", " + repr(pop3)
     assert pops == '5, 4, 3'

def test_linked_list_pop_empty():
     with pytest.raises(ValueError):
        my_list = LinkedList([])
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
    with pytest.raises(ValueError):
        my_list = LinkedList([1, 2, 3, 4])
        my_list.remove(5)

def test_linked_list_len():
    my_list = LinkedList([1, 2, 3, 4, 5])
    assert len(my_list) == 5    
    my_list = LinkedList([1, 2, 3, 4])
    assert len(my_list) == 4    
    my_list = LinkedList([1, 2, 3])
    assert len(my_list) == 3    
    my_list = LinkedList([1, 2])
    assert len(my_list) == 2    
    my_list = LinkedList([1])
    assert len(my_list) == 1

def test_linked_list_str():
    my_list = LinkedList([1, 2, 3])
    assert str(my_list) == '(3, 2, 1)'
    assert str(my_list.head.value) == '3'
    assert str(my_list.head.next.value) == '2'
    assert str(my_list.head.next.next.value) == '1'
    assert str(my_list.head.next.next.next) == 'None'

def test_linked_list_size():
    my_list = LinkedList([1, 2, 3, 4, 5])
    assert my_list.size() == 5    
    my_list = LinkedList([1, 2, 3, 4])
    assert my_list.size() == 4    
    my_list = LinkedList([1, 2, 3])
    assert my_list.size() == 3    
    my_list = LinkedList([1, 2])
    assert my_list.size() == 2    
    my_list = LinkedList([1])
    assert my_list.size() == 1

def capture_output_for_print_test(func):
    def wrapper(*args, **kwargs):
        output_buffer = io.StringIO()
        sys.stdout = output_buffer

        try:
            func(*args, **kwargs)
        finally:
            sys.stdout = sys.__stdout__
            captured_output = output_buffer.getvalue()
            output_buffer.close()

        return captured_output

    return wrapper

def test_linked_list_print():
    linked_list = LinkedList([1, 2, 3, 4, 5])
    print(linked_list)
    captured_output = capture_output_for_print_test(print)(linked_list)
    expected_output = "(5, 4, 3, 2, 1)"
    assert captured_output.strip() == expected_output