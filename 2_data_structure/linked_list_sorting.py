

# Use this class as the nodes in your linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class SortedLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """
        Append a value to the Linked List in ascending sorted order

        Args:
           value(int): Value to add to Linked List
        """


        # If LinkedList is empty
        if self.head is None:
            self.head = Node(value)
            return

        if self.head.value > value:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            return


        # Create a temporary Node object
        node = self.head

        # Iterate till the end of the currrent LinkedList
        while node.next is not None and value >= node.next.value:
            node = node.next

        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node



    def to_list(self):
        out = []          # <-- Declare a Python list
        node = self.head  # <-- Create a temporary Node object

        while node:       # <-- Iterate untill we have nodes available
            out.append(int(str
                (node.value))) # <-- node.value is actually of type Node, therefore convert it into int before appending to the Python list
            node = node.next

        return out


if __name__ == "__main__":
    # Test cases
    linked_list = SortedLinkedList()
    linked_list.append(3)
    print("Pass" if (linked_list.head.value == 3) else "Fail")

    linked_list.append(2)
    print("Pass" if (linked_list.head.value == 2) else "Fail")

    linked_list.append(4)
    node = linked_list.head.next.next
    print("Pass" if (node.value == 4) else "Fail")

    linked_list.append(0)
    linked_list.append(-4)
    linked_list.append(10)
    linked_list.append(1)
    print(linked_list.to_list())