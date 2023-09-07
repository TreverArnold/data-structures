# Data Structures
Holds sample code for a number of classic data structures implemented in Python.

## LinkedList:
#### Module: [linked_list.py](linked_list.py)
#### Tests:[linked_list_.py](linked_list_test.py)
    * push(val): Inserts the value at the head of the list
    * pop(): Pops the first value off the head of the list and returns it. Raises an exception if there are no values to return.
    * size(): Returns the length of the list.
    * search(val): Returns the node containing the val in the list if it is present. If it is not present it will return None.
    * remove(node): Removes the given node from the list. If the node is not in the list is will raise an exception.
    * display(): Returns a unicode string representing the list as if it were a Python tuple literal. Ex: "(5, 'Bravo', 9)"
    * len(the_list): Returns the size of the list
    * print(the_list): Returns what the display method returns.