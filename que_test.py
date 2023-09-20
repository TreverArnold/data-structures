import pytest

from que_ import Queue


def test_innit():
    my_queue = Queue([1, 2, 3])
    assert my_queue.front.value == 1
    assert my_queue.front.next.value == 2 
    assert my_queue.rear.value == 3
    assert my_queue.size_count == 3
 
def test_enqueue():
    my_queue = Queue()
    my_queue.enqueue(1)
    assert my_queue.front.value == 1
    assert my_queue.rear.value == 1
    assert my_queue.size_count == 1
    my_queue.enqueue(2)
    assert my_queue.front.value == 1
    assert my_queue.rear.value == 2
    assert my_queue.size_count == 2
    my_queue.enqueue(3)
    assert my_queue.front.value == 1
    assert my_queue.front.next.value == 2 
    assert my_queue.rear.value == 3
    assert my_queue.size_count == 3

def test_dequeue():
    my_queue = Queue([1, 2, 3])
    assert my_queue.front.value == 1
    assert my_queue.front.next.value == 2 
    assert my_queue.rear.value == 3
    assert my_queue.size_count == 3
    assert my_queue.dequeue() == 1
    assert my_queue.size_count == 2
    assert my_queue.front.value == 2
    assert my_queue.rear.value == 3
    assert my_queue.dequeue() == 2
    assert my_queue.size_count == 1
    assert my_queue.front.value == 3
    assert my_queue.rear.value == 3
    assert my_queue.dequeue() == 3
    assert my_queue.size_count == 0
    assert my_queue.front == None
    assert my_queue.rear == None
    with pytest.raises(ValueError, match="Queue is empty. Cannot dequeue."):
            my_queue.dequeue()

def test_peek():
    my_queue = Queue([1, 2, 3])
    assert my_queue.front.value == 1
    assert my_queue.front.next.value == 2 
    assert my_queue.rear.value == 3
    assert my_queue.size_count == 3
    assert my_queue.peek() == 2
    assert my_queue.front.value == 1
    assert my_queue.front.next.value == 2 
    assert my_queue.rear.value == 3
    assert my_queue.size_count == 3
    my_queue = Queue()
    assert my_queue.peek() == None
    assert my_queue.front == None
    assert my_queue.rear == None
    assert my_queue.size_count == 0

def test_len():
    my_queue = Queue()
    assert len(my_queue) == 0
    my_queue.enqueue(1)
    assert len(my_queue) == 1
    my_queue.enqueue(2)
    assert len(my_queue) == 2
    my_queue.enqueue(3)
    assert len(my_queue) == 3
    my_queue.dequeue()
    assert len(my_queue) == 2
    my_queue.dequeue()
    assert len(my_queue) == 1
    my_queue.dequeue()
    assert len(my_queue) == 0

def test_size():
    my_queue = Queue()
    assert my_queue.size() == 0
    my_queue.enqueue(1)
    assert my_queue.size() == 1
    my_queue.enqueue(2)
    assert my_queue.size() == 2
    my_queue.enqueue(3)
    assert my_queue.size() == 3
    my_queue.dequeue()
    assert my_queue.size() == 2
    my_queue.dequeue()
    assert my_queue.size() == 1
    my_queue.dequeue()
    assert my_queue.size() == 0