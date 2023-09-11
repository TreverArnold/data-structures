import pytest

from stack import Stack

def test_stack_innit():
    my_stack = Stack([1, 2, 3])
    assert my_stack._size == 3
    assert my_stack.top.value == 3
    assert my_stack.top.next.value == 2
    assert my_stack.top.next.next.value == 1
    assert my_stack.top.next.next.next == None

def test_stack_innit_empty():
    my_stack = Stack()
    assert my_stack._size == 0
    assert my_stack.top == None

def test_stack_push():
    my_stack = Stack([1, 2, 3])
    my_stack.push('hello')
    assert my_stack._size == 4
    assert my_stack.top.value == 'hello'

def test_stack_push_empty():
    my_stack = Stack([1, 2, 3])
    my_stack.push('')
    assert my_stack._size == 4
    assert my_stack.top.value == ''

def test_stack_pop():
    my_stack = Stack([1, 2, 3])
    assert my_stack.top.value == 3
    assert my_stack.pop() == 3
    assert my_stack._size == 2
    assert my_stack.top.value == 2
    assert my_stack.pop() == 2
    assert my_stack._size == 1
    assert my_stack.top.value == 1

def test_stack_pop_empty():
    with pytest.raises(ValueError, match=('Pop does not work on an empty list')):
        my_stack = Stack()
        my_stack.pop()

def test_stack_size():
    my_stack = Stack([1, 2])
    assert my_stack.size() == 2
    my_stack.pop()
    assert my_stack.size() == 1
    my_stack.pop()
    assert my_stack.size() == 0
    my_stack.push(1)
    assert my_stack.size() == 1
    my_stack.push(2)
    assert my_stack.size() == 2

def test_stack_len():
    my_stack = Stack([1, 2])
    assert my_stack.__len__() == 2
    my_stack.pop()
    assert my_stack.__len__() == 1
    my_stack.pop()
    assert my_stack.__len__() == 0
    my_stack.push(1)
    assert my_stack.__len__() == 1
    my_stack.push(2)
    assert my_stack.__len__() == 2
