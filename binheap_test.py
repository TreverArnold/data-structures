from binheap import BinHeap


def test_binheap_innit():
    my_heap = BinHeap([1, 2, 3, 4, 5, 6, 7])
    assert my_heap.top.value == 1
    assert my_heap.top.leftchild.value == 2
    assert my_heap.top.rightchild.value == 3
    assert my_heap.top.leftchild.leftchild.value == 4
    assert my_heap.top.leftchild.rightchild.value == 5
    assert my_heap.top.rightchild.leftchild.value == 6
    assert my_heap.top.rightchild.rightchild.value == 7


def test_binheap_pop():
    my_heap = BinHeap([1, 2, 3, 4, 5, 6, 7])
    assert my_heap.pop() == 1
    assert my_heap.pop() == 2
    assert my_heap.pop() == 3
    assert my_heap.pop() == 4
    assert my_heap.pop() == 5
    assert my_heap.pop() == 6
    assert my_heap.pop() == 7


def test_binheap_push():
    my_heap = BinHeap()
    my_heap.push(1)
    assert my_heap.top.value == 1
    my_heap.push(2)
    assert my_heap.top.value == 1
    assert my_heap.top.leftchild.value == 2
    my_heap.push(3)
    assert my_heap.top.value == 1
    assert my_heap.top.leftchild.value == 2
    assert my_heap.top.rightchild.value == 3
    my_heap.push(4)
    assert my_heap.top.value == 1
    assert my_heap.top.leftchild.value == 2
    assert my_heap.top.rightchild.value == 3
    assert my_heap.top.leftchild.leftchild.value == 4
    my_heap.push(5)
    assert my_heap.top.value == 1
    assert my_heap.top.leftchild.value == 2
    assert my_heap.top.rightchild.value == 3
    assert my_heap.top.leftchild.leftchild.value == 4
    assert my_heap.top.leftchild.rightchild.value == 5
    my_heap.push(6)
    assert my_heap.top.value == 1
    assert my_heap.top.leftchild.value == 2
    assert my_heap.top.rightchild.value == 3
    assert my_heap.top.leftchild.leftchild.value == 4
    assert my_heap.top.leftchild.rightchild.value == 5
    assert my_heap.top.rightchild.leftchild.value == 6
    my_heap.push(7)
    assert my_heap.top.value == 1
    assert my_heap.top.leftchild.value == 2
    assert my_heap.top.rightchild.value == 3
    assert my_heap.top.leftchild.leftchild.value == 4
    assert my_heap.top.leftchild.rightchild.value == 5
    assert my_heap.top.rightchild.leftchild.value == 6
    assert my_heap.top.rightchild.rightchild.value == 7
