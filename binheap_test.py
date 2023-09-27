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


def test_binheap_1():
    my_heap = BinHeap()
    my_heap.push(15)
    #      15
    assert my_heap.top.value == 15
    my_heap.push(11)
    #      15
    #     /
    #    11
    # heapify-up
    # 15 <--> 11
    #      11
    #     /
    #    15
    assert my_heap.top.value == 11
    assert my_heap.top.leftchild.value == 15
    assert my_heap.top.rightchild is None
    my_heap.push(8)
    #      11
    #     /  \
    #    15   8
    # heapify-up
    # 11 <--> 8
    #      8
    #     /  \
    #    15   11
    assert my_heap.top.value == 8
    assert my_heap.top.leftchild.value == 15
    assert my_heap.top.leftchild.leftchild is None
    assert my_heap.top.leftchild.rightchild is None
    assert my_heap.top.rightchild.value == 11
    assert my_heap.top.rightchild.leftchild is None
    assert my_heap.top.rightchild.rightchild is None
    my_heap.push(5)
    #      8
    #     /  \
    #    15   11
    #   /
    #  5
    # heapify-up
    # 5 <--> 15, 5 <--> 8
    #      5
    #     /  \
    #    8   11
    #   /
    #  15
    assert my_heap.top.value == 5
    assert my_heap.top.leftchild.value == 8
    assert my_heap.top.rightchild.value == 11
    assert my_heap.top.rightchild.leftchild is None
    assert my_heap.top.rightchild.rightchild is None
    assert my_heap.top.leftchild.leftchild.value == 15
    assert my_heap.top.leftchild.rightchild is None
    assert my_heap.top.leftchild.leftchild.rightchild is None
    assert my_heap.top.leftchild.leftchild.leftchild is None
    my_heap.push(3)
    #      5
    #     /  \
    #    8   11
    #   / \
    #  15  3
    # heapify-up
    # 3 <--> 8, 3 <--> 5
    #      3
    #     /  \
    #    5   11
    #   / \
    #  15  8
    assert my_heap.top.value == 3
    assert my_heap.top.leftchild.value == 5
    assert my_heap.top.rightchild.value == 11
    assert my_heap.top.rightchild.leftchild is None
    assert my_heap.top.rightchild.rightchild is None
    assert my_heap.top.leftchild.leftchild.value == 15
    assert my_heap.top.leftchild.rightchild.value == 8
    assert my_heap.top.leftchild.leftchild.rightchild is None
    assert my_heap.top.leftchild.leftchild.leftchild is None
    assert my_heap.top.leftchild.rightchild.rightchild is None
    assert my_heap.top.leftchild.rightchild.leftchild is None
    my_heap.push(4)
    #      3
    #     /  \
    #    5    11
    #   / \   /
    #  15 8  4
    # heapify-up
    # 4 <--> 11
    #      3
    #     /  \
    #    5    4
    #   / \   /
    #  15 8  11
    assert my_heap.top.value == 3
    assert my_heap.top.leftchild.value == 5
    assert my_heap.top.rightchild.value == 4
    assert my_heap.top.rightchild.leftchild.value == 11
    assert my_heap.top.rightchild.leftchild.rightchild is None
    assert my_heap.top.rightchild.leftchild.leftchild is None
    assert my_heap.top.rightchild.rightchild is None
    assert my_heap.top.leftchild.leftchild.value == 15
    assert my_heap.top.leftchild.rightchild.value == 8
    assert my_heap.top.leftchild.leftchild.rightchild is None
    assert my_heap.top.leftchild.leftchild.leftchild is None
    assert my_heap.top.leftchild.rightchild.rightchild is None
    assert my_heap.top.leftchild.rightchild.leftchild is None
