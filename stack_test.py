import pytest

from stack import Stack

def test_stack_push():
    my_stack = Stack([1, 2, 3])
    my_stack.push('hello')
    assert len(my_stack) == 4

def test_stack_push_empty():
    my_stack = Stack([1, 2, 3])
    my_stack.push('')
    assert len(my_stack) == 4

def test_stack_pop():
    my_stack = Stack([1, 2, 3])
    assert my_stack.pop() == 3
    assert len(my_stack) == 2
    assert my_stack.pop() == 2
    assert len(my_stack) == 1

def test_stack_pop_empty():
    with pytest.raises(ValueError, match=('Cannot pop from an empty stack')):
        my_stack = Stack()
        my_stack.pop()
