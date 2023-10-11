# Data Structures
Holds sample code for a number of classic data structures implemented in Python.

## LinkedList:
#### Module: [linked_list.py](linked_list.py)
#### Tests: [linked_list_test.py](linked_list_test.py)
    * push(val): Inserts the value at the head of the list.
    * pop(): Pops the first value off the head of the list and returns it. Raises an exception if there are no values to return.
    * size(): Returns the length of the list.
    * search(val): Returns the node containing the val in the list if it is present. If it is not present it will return None.
    * remove(node): Removes the given node from the list. If the node is not in the list is will raise an exception.
    * display(): Returns a unicode string representing the list as if it were a Python tuple literal. Ex: "(5, 'Bravo', 9)"
    * len(the_list): Returns the size of the list.
    * print(the_list): Returns what the display method returns.

## DoublyLinkedList:
#### Module: [doubly_linked_list.py](doubly_linked_list.py)
#### Tests: [doubly_linked_list_test.py](doubly_linked_list_test.py)
    * push(val): Inserts the value at the head of the list.
    * append(val): Insterts the value at the tail of the list.
    * pop(): Pops the first value off the head of the list and returns it. Raises an exception if there are no values to return.
    * shift(): Shifts the last value off the tail of the list and returns it. Raises an exception if there are no values to shift.
    * remove(node): Removes the given node from the list. If the node is not in the list is will raise an exception.
    * len(the_list): Returns the size of the list.
    
## Stack:
#### Module: [stack.py](stack.py)
#### Tests: [stack_test.py](stack_test.py)
    * push(val): Inserts the value at the top of the stack.
    * pop(): Pops the top value off of the stack, returns a value error if there is no top value.
    * size(): Returns the height of the stack.
    * len(the_list): Returns the size of the stack.

## Queue:
#### Module: [queue.py](que_.py)
#### Tests: [queue_test.py](que_test.py)
    * enqueue(val): Adds a value to the rear of the queue
    * dequeue: Removes and returns first value(front) of the queue, returns a value error if there is no front value.
    * size(): Returns the length of the queue.
    * len(the_list): Returns the size of the queue.

## Deueue:
#### Module: [dequeue.py](deque.py)
#### Tests: [dequeue_test.py](deque_test.py)
    * append(val): adds value to the end of the deque
    * appendleft(val): adds a value to the front of the deque
    * pop(): removes a value from the end of the deque and returns it (raises an exception if the deque is empty)
    * popleft(): removes a value from the front of the deque and returns it (raises an exception if the deque is empty)
    * peek(): returns the next value that would be returned by pop but leaves the value in the deque (returns None if the deque is empty)
    * peekleft(): returns the next value that would be returned by popleft but leaves the value in the deque (returns None if the deque is empty)
    * size(): returns the count of items in the queue (returns 0 if the queue is empty)

## BinHeap:
#### Module: [binheap.py](binheap.py)
#### Tests: [binheap_test.py](binheap_test.py)
    * push(val): puts a new value into the heap, maintaining the heap property.
    * pop(): removes the “top” value in the heap, maintaining the heap property.

## PriorityQueue:
#### Module: [priority_queue.py](priority_queue.py)
#### Tests: [priority_queue_test.py](priority_queue_test.py)
    * insert(value, priority): inserts a value into the queue. Takes an optional argument for that value’s priority, set by default to whatever your lowest priority is
    * pop(): removes the most important item from the queue and returns its value.
    * peek(): returns the most important item without removing it from the queue.

## Graph
### Module
### Tests: 
    * g.nodes(): return a list of all nodes in the graph
    * g.edges(): return a list of all edges in the graph
    * g.add_node(val): adds a new node with value ‘n’ to the graph
    * g.add_edge(val1, val2): adds a new edge to the graph connecting the node containing ‘val1’ and the node containing ‘val2’. If either val1 or val2 are not already present in the graph, they should be added. If an edge already exists, overwrite it.
    * g.del_node(val): deletes the node containing ‘val’ from the graph; raises an error if no such node exists
    * g.del_edge(val1, val2): deletes the edge connecting ‘val1’ and ‘val2’ from the graph; raises an error if no such edge exists
    * g.has_node(val): True if node containing ‘val’ is contained in the graph, False if not.
    * g.neighbors(val): returns the list of all nodes connected to the node containing ‘val’ by edges; raises an error if val is not in g
    * g.adjacent(val1, val2): returns True if there is an edge connecting val1 and val2, False if not; raises an error if either of the supplied values are not in g