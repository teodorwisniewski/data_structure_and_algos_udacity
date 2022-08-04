

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        previous_head = self.head
        self.head = Node(value)
        self.head.next = previous_head

    def append(self, value):
        """ Append a value to the end of the list. """
        if self.head is None:
            self.head = Node(value)
            return

        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = Node(value)

    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """

        last_node = self.head
        while last_node.next is not None:
            if last_node.value == value:
                return last_node
            last_node = last_node.next
        return

    def remove(self, value):
        """ Remove first occurrence of value. """
        if self.head is not None and self.head.next is None and self.head.value == value:
            self.head = None
            return
        elif self.head is not None and self.head.value == value:
            self.head = self.head.next
            return

        last_node = self.head
        while last_node.next is not None:
            if last_node.next.value == value:
                if last_node.next.next is not None:
                    last_node.next = last_node.next.next
                    return
                else:
                    last_node.next = None
                    return
            last_node = last_node.next
        return

    def pop(self):
        """ Return the first node's value and remove it from the list. """
        if self.head is not None:
            popped_head = self.head
            self.head = self.head.next
            return popped_head.value




if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.prepend(1)
    print(linked_list.to_list())
    linked_list.append(3)
    linked_list.prepend(2)
    print(linked_list.to_list())
    linked_list.prepend(2)
    linked_list.prepend(1)
    linked_list.append(4)
    linked_list.append(3)
    print(linked_list.search(1).value)
    print(linked_list.search(4).value)
    print(linked_list.to_list())
    print("Removing 1 from the linked list")
    linked_list.remove(1)
    print(linked_list.to_list())
    print("Removing 2 from the linked list")
    linked_list.remove(2)
    print(linked_list.to_list())
    print("Removing 4 from the linked list")
    linked_list.remove(4)
    print(linked_list.to_list())
    print("Removing 3 from the linked list")
    linked_list.remove(3)
    print(linked_list.to_list())
    print("Removing 3 from the linked list")
    linked_list.remove(3)
    print(linked_list.to_list())
    value = linked_list.pop()
    print(f"popped value is {value}")
    print(linked_list.to_list())
