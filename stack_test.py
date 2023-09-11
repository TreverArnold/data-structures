import pytest

from stack import Stack

def test_stack_push():
    my_stack = Stack([1, 2, 3])
    my_stack.push('hello')
    assert my_stack._storage._size == 4

def test_stack_push_empty():
    my_stack = Stack([1, 2, 3])
    my_stack.push('')
    assert my_stack._storage._size == 4

def test_stack_pop():
    my_stack = Stack([1, 2, 3])
    assert my_stack.pop() == 3
    assert my_stack._storage._size == 2
    assert my_stack.pop() == 2
    assert my_stack._storage._size == 1

def test_stack_pop_empty():
    with pytest.raises(ValueError, match=('Pop does not work on an empty list')):
        my_stack = Stack()
        my_stack.pop()
