


# Helper code

# A class behaves like a data-type, just like an int, float or any other built-in ones.
# User defined class
class Node:
    def __init__(self, value): # <-- For simple LinkedList, "value" argument will be an int, whereas, for NestedLinkedList, "value" will be a LinkedList
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

# User defined class
class LinkedList:
    def __init__(self, head): # <-- Expects "head" to be a Node made up of an int or LinkedList
        self.head = head

    '''
    For creating a simple LinkedList, we will pass an integer as the "value" argument
    For creating a nested LinkedList, we will pass a LinkedList as the "value" argument
    '''
    def append(self, value):

        # If LinkedList is empty
        if self.head is None:
            self.head = Node(value)
            return

        # Create a temporary Node object
        node = self.head

        # Iterate till the end of the currrent LinkedList
        while node.next is not None:
            node = node.next

        # Append the newly creataed Node at the end of the currrent LinkedList
        node.next = Node(value)


    '''We will need this function to convert a LinkedList object into a Python list of integers'''
    def to_list(self):
        out = []          # <-- Declare a Python list
        node = self.head  # <-- Create a temporary Node object

        while node:       # <-- Iterate untill we have nodes available
            out.append(int(str
                (node.value))) # <-- node.value is actually of type Node, therefore convert it into int before appending to the Python list
            node = node.next

        return out



def merge(list1, list2):
    merged = LinkedList(None)
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    list1_elt = list1.head
    list2_elt = list2.head
    while list1_elt is not None or list2_elt is not None:
        if list1_elt is None:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
        elif list2_elt is None:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        elif list1_elt.value <= list2_elt.value:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        else:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
    return merged


''' In a NESTED LinkedList object, each node will be a simple LinkedList in itself'''


class NestedLinkedList(LinkedList):
    def flatten(self):
        return self._flatten(self.head)  # <-- self.head is a node for NestedLinkedList

    '''  A recursive function '''

    def _flatten(self, node):
        # A termination condition
        if node.next is None:
            return merge(node.value, None)  # <-- First argument is a simple LinkedList

        # _flatten() is calling itself untill a termination condition is achieved
        return merge(node.value, self._flatten(node.next))  # <-- Both arguments are a simple LinkedList each


if __name__ == "__main__":
    ''' Test merge() function'''
    linked_list = LinkedList(Node(1))
    linked_list.append(3)
    linked_list.append(5)

    second_linked_list = LinkedList(Node(2))
    second_linked_list.append(4)

    merged = merge(linked_list, second_linked_list)
    node = merged.head
    while node is not None:
        # This will print 1 2 3 4 5
        print(node.value)
        node = node.next

    # Lets make sure it works with a None list
    merged = merge(None, linked_list)
    node = merged.head
    while node is not None:
        # This will print 1 3 5
        print(node.value)
        node = node.next

    ''' Test flatten() function'''
    # Create a nested linked list with one node.
    # The node itself is a simple linked list as 1-->3-->5 created previously
    nested_linked_list = NestedLinkedList(Node(linked_list))

    # Append a node (a linked list as 2-->4) to the existing nested linked list
    nested_linked_list.append(second_linked_list)

    # Call the `flatten()` function
    flattened = nested_linked_list.flatten()

    # Logic to print the flattened list
    node = flattened.head
    while node is not None:
        # This will print 1 2 3 4 5
        print(node.value)
        node = node.next