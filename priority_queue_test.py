import pytest

from priority_queue import PriorityQueue


def test_init_():
    pq = PriorityQueue([("apple", 1), ["banana", 1], ("avocado", 2), ["peach", 4]])
    assert pq.pop() == "apple"
    assert pq.pop() == "banana"
    assert pq.pop() == "avocado"
    assert pq.pop() == "peach"


def test_insert_pop_peek():
    pq = PriorityQueue()
    pq.insert("apple", 1)
    assert pq.peek() == "apple"
    pq.insert("banana", 1)
    pq.insert("avocado", 1)
    pq.insert("peach", 1)
    assert pq.peek() == "apple"
    assert pq.pop() == "apple"
    assert pq.peek() == "banana"
    assert pq.pop() == "banana"
    assert pq.peek() == "avocado"
    assert pq.pop() == "avocado"
    assert pq.peek() == "peach"
    assert pq.pop() == "peach"
    pq = PriorityQueue()
    pq.insert("apple", 1)
    assert pq.peek() == "apple"
    pq.insert("banana", 3)
    pq.insert("avocado", 1)
    pq.insert("peach", 4)
    assert pq.peek() == "apple"
    assert pq.pop() == "apple"
    assert pq.peek() == "avocado"
    assert pq.pop() == "avocado"
    assert pq.peek() == "banana"
    assert pq.pop() == "banana"
    assert pq.peek() == "peach"
    assert pq.pop() == "peach"


def test_peek_none():
    pq = PriorityQueue()
    assert pq.peek() == None


def test_pop_none():
    pq = PriorityQueue()
    with pytest.raises(ValueError, match=("Cannot pop from an empty priority queue")):
        assert pq.pop()


def test_no_priority():
    pq = PriorityQueue(["apple", "banana", "avocado", "peach"])
    pq.pop() == "apple"
    pq.pop() == "banana"
    pq.pop() == "avocado"
    pq.pop() == "peach"
    pq.insert("apple")


def test_insert_list_tuple():
    pq = PriorityQueue(
        [([1, 2, 3], 1), [("tree", "apple"), 1], ([1, 2, 7, 7], 2), [("h", "y", 6), 4]]
    )
    assert pq.pop() == [1, 2, 3]
    assert pq.pop() == ("tree", "apple")
    assert pq.pop() == [1, 2, 7, 7]
    assert pq.pop() == ("h", "y", 6)
    pq.insert([1, 2, 3])
    pq.insert((3, 2, 1))
    assert pq.pop() == [1, 2, 3]
    assert pq.pop() == (3, 2, 1)
    pq = PriorityQueue([[1, 2, 3], 2, ("hi", -1)])
    assert pq.pop() == "hi"
    assert pq.pop() == [1, 2, 3]
    assert pq.pop() == 2
