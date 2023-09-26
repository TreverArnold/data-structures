import pytest

from deque import Deque


def test_init():
    my_queue = Deque([1, 2, 3])
    assert len(my_queue) == 3
    assert my_queue.popleft() == 1
    assert my_queue.popleft() == 2
    assert my_queue.popleft() == 3
    assert len(my_queue) == 0


def test_append_left_pop_left():
    my_queue = Deque()
    my_queue.appendleft(1)
    assert len(my_queue) == 1
    assert my_queue.popleft() == 1
    my_queue.appendleft(1)
    my_queue.appendleft(2)
    assert len(my_queue) == 2
    assert my_queue.popleft() == 2
    assert my_queue.popleft() == 1
    my_queue.appendleft(1)
    my_queue.appendleft(2)
    my_queue.appendleft(3)
    assert len(my_queue) == 3
    assert my_queue.popleft() == 3
    assert my_queue.popleft() == 2
    assert my_queue.popleft() == 1
    with pytest.raises(ValueError, match="Popleft does not work on an empty queue"):
        my_queue.popleft()


def test_append_pop():
    my_queue = Deque()
    my_queue.append(1)
    assert len(my_queue) == 1
    assert my_queue.pop() == 1
    my_queue.append(1)
    my_queue.append(2)
    assert len(my_queue) == 2
    assert my_queue.pop() == 2
    assert my_queue.pop() == 1
    my_queue.append(1)
    my_queue.append(2)
    my_queue.append(3)
    assert len(my_queue) == 3
    assert my_queue.pop() == 3
    assert my_queue.pop() == 2
    assert my_queue.pop() == 1
    with pytest.raises(ValueError, match="Pop does not work on an empty queue"):
        my_queue.pop()


def test_peek_left():
    my_queue = Deque([1, 2, 3, 4])
    assert my_queue.peekleft() == 1
    assert len(my_queue) == 4
    my_queue = Deque()
    my_queue.peek() == None
    assert len(my_queue.dll) == 0


def test_peek():
    my_queue = Deque([1, 2, 3, 4])
    assert my_queue.peek() == 4
    assert len(my_queue) == 4
    my_queue = Deque()
    my_queue.peek() == None
    assert len(my_queue.dll) == 0


def test_len():
    my_queue = Deque()
    assert len(my_queue) == 0
    my_queue.appendleft(1)
    assert len(my_queue) == 1
    my_queue.appendleft(2)
    assert len(my_queue) == 2
    my_queue.appendleft(3)
    assert len(my_queue) == 3
    my_queue.popleft()
    assert len(my_queue) == 2
    my_queue.popleft()
    assert len(my_queue) == 1
    my_queue.popleft()
    assert len(my_queue) == 0
    my_queue.append(1)
    assert len(my_queue) == 1
    my_queue.append(2)
    assert len(my_queue) == 2
    my_queue.append(3)
    assert len(my_queue) == 3
    my_queue.pop()
    assert len(my_queue) == 2
    my_queue.pop()
    assert len(my_queue) == 1
    my_queue.pop()
    assert len(my_queue) == 0


def test_size():
    my_queue = Deque()
    assert my_queue.size() == 0
    my_queue.appendleft(1)
    assert my_queue.size() == 1
    my_queue.appendleft(2)
    assert my_queue.size() == 2
    my_queue.appendleft(3)
    assert my_queue.size() == 3
    my_queue.popleft()
    assert my_queue.size() == 2
    my_queue.popleft()
    assert my_queue.size() == 1
    my_queue.popleft()
    assert my_queue.size() == 0
    my_queue.append(1)
    assert my_queue.size() == 1
    my_queue.append(2)
    assert my_queue.size() == 2
    my_queue.append(3)
    assert my_queue.size() == 3
    my_queue.pop()
    assert my_queue.size() == 2
    my_queue.pop()
    assert my_queue.size() == 1
    my_queue.pop()
    assert my_queue.size() == 0