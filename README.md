# Data Structures
Holds sample code for a number of classic data structures implemented in Python.

## LinkedList:
#### Module: [linked_list.py](linked_list.py)
#### Tests: [linked_list_test.py](linked_list_test.py)
    * push(val): Inserts the value at the head of the list
    * pop(): Pops the first value off the head of the list and returns it. Raises an exception if there are no values to return.
    * size(): Returns the length of the list.
    * search(val): Returns the node containing the val in the list if it is present. If it is not present it will return None.
    * remove(node): Removes the given node from the list. If the node is not in the list is will raise an exception.
    * display(): Returns a unicode string representing the list as if it were a Python tuple literal. Ex: "(5, 'Bravo', 9)"
    * len(the_list): Returns the size of the list
    * print(the_list): Returns what the display method returns.

## doublyLinkedList:
#### Module: [doubly_linked_list.py](doubly_linked_list.py)
#### Tests: [doubly_linked_list_test.py](doubly_linked_list_test.py)
    * push(val): Inserts the value at the head of the list
    * append(val): Insterts the value at the tail of the list
    * pop(): Pops the first value off the head of the list and returns it. Raises an exception if there are no values to return.
    * shift(): Shifts the last value off the tail of the list and returns it. Raises an exception if there are no values to shift
    * remove(node): Removes the given node from the list. If the node is not in the list is will raise an exception.
    * len(the_list): Returns the size of the list
    
## Stack:
#### Module: [stack.py](stack.py)
#### Tests: [stack_tets.py](stack_test.py)
    * push(val): Inserts the value at the top of the stack
    * pop(): Pops the top value off of the stack, returns a value error if there is no top value
    * size(): Returns the height of the stack.
    * len(the_list): Returns the size of the stack