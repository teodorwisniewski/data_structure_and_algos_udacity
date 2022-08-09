"""
Doubly linked list exercice
"""

def getNodeValuesHeadToTail(linkedList):
    values = []
    node = linkedList.head
    while node is not None:
        values.append(node.value)
        node = node.next
    print(values)
    return values


def getNodeValuesTailToHead(linkedList):
    values = []
    node = linkedList.tail
    while node is not None:
        values.append(node.value)
        node = node.prev
    print(values)
    return values


def bindNodes(node_one, node_two):
    node_one.next = node_two
    node_two.prev = node_one




# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if node.next is not None or node.prev is not None:
            self.remove(node)
        old_head = self.head
        if old_head is not None:
            self.head = node
            self.head.next = old_head
            old_head.prev = self.head
            self.head.prev = None
        else:
            self.head = node

    def setTail(self, node):
        if node.next is not None or node.prev is not None:
            self.remove(node)
        old_tail = self.tail
        if old_tail is not None:
            self.tail = node
            self.tail.next = None
            self.tail.prev = old_tail
            old_tail.next = self.tail
        else:
            self.tail = node
            self.head = node

    def insertBefore(self, node, node_to_insert):
        if node_to_insert.next is not None or node_to_insert.prev is not None:
            self.remove(node_to_insert)
        if node.prev is None:
            self.setHead(node_to_insert)
        else:
            old_prev = node.prev
            node.prev = node_to_insert
            node_to_insert.next = node
            node_to_insert.prev = old_prev
            old_prev.next = node_to_insert

    def insertAfter(self, node, node_to_insert):
        if node_to_insert.next is not None or node_to_insert.prev is not None:
            self.remove(node_to_insert)
        if node.next is None:
            self.setTail(node_to_insert)
        else:
            old_next = node.next
            node.next = node_to_insert
            node_to_insert.next = old_next
            node_to_insert.prev = node
            old_next.prev = node_to_insert

    def insertAtPosition(self, position, node_to_insert):
        # Write your code here.
        pass

    def removeNodesWithValue(self, value):
        # Write your code here.
        pass

    def remove(self, node):
        if node.next is not None and node.prev is not None:
            # removing a node from the middle of the list
            next_temp = node.next
            prev_temp = node.prev
            prev_temp.next = next_temp
            next_temp.prev = prev_temp
            node.next = None
            node.prev = None
        elif node.next is not None and node.prev is None:
            # removing head
            new_head = node.next
            new_head.prev = None
            head = new_head
            node.next = None
            node.prev = None
        elif node.next is None and node.prev is not None:
            # removing tail
            new_tail = node.prev
            new_tail.next = None
            self.tail = new_tail
            node.next = None
            node.prev = None


    def containsNodeWithValue(self, value):
        # Write your code here.
        pass


if __name__ == "__main__":
    linkedList = DoublyLinkedList()
    one = Node(1)
    two = Node(2)
    three = Node(3)
    three2 = Node(3)
    three3 = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    bindNodes(one, two)
    bindNodes(two, three)
    bindNodes(three, four)
    bindNodes(four, five)
    linkedList.head = one
    linkedList.tail = five

    linkedList.setHead(four)

    assert getNodeValuesHeadToTail(linkedList) == [4, 1, 2, 3, 5]
    assert getNodeValuesTailToHead(linkedList) == [5, 3, 2, 1, 4]

    # linkedList.setHead(five)
    # assert getNodeValuesHeadToTail(linkedList) == [5, 4, 1, 2, 3]
    # assert getNodeValuesTailToHead(linkedList) == [3, 2, 1, 4, 5]
    #
    # linkedList.setHead(five)
    # assert getNodeValuesHeadToTail(linkedList) == [5, 4, 1, 2, 3]
    # assert getNodeValuesTailToHead(linkedList) == [3, 2, 1, 4, 5]

    linkedList.setTail(six)
    assert getNodeValuesHeadToTail(linkedList) == [4, 1, 2, 3, 5, 6]
    assert getNodeValuesTailToHead(linkedList) == [6, 5, 3, 2, 1, 4]

    linkedList.insertBefore(six, three)
    assert getNodeValuesHeadToTail(linkedList) == [4, 1, 2, 5, 3, 6]
    assert getNodeValuesTailToHead(linkedList) == [6, 3, 5, 2, 1, 4]

    linkedList.insertAfter(six, three2)
    assert getNodeValuesHeadToTail(linkedList) == [4, 1, 2, 5, 3, 6, 3]
    assert getNodeValuesTailToHead(linkedList) == [3, 6, 3, 5, 2, 1, 4]

    linkedList.insertAfter(one, three2)
    assert getNodeValuesHeadToTail(linkedList) == [4, 1, 3, 2, 5, 3, 6]
    assert getNodeValuesTailToHead(linkedList) == [6, 3, 5, 2, 3, 1, 4]

    linkedList.insertAtPosition(1, three3)
    assert getNodeValuesHeadToTail(linkedList) == [3, 4, 1, 2, 5, 3, 6, 3]
    assert getNodeValuesTailToHead(linkedList) == [3, 6, 3, 5, 2, 1, 4, 3]

    linkedList.removeNodesWithValue(3)
    assert getNodeValuesHeadToTail(linkedList) == [4, 1, 2, 5, 6]
    assert getNodeValuesTailToHead(linkedList) == [6, 5, 2, 1, 4]

    linkedList.remove(two)
    assert getNodeValuesHeadToTail(linkedList) == [4, 1, 5, 6]
    assert getNodeValuesTailToHead(linkedList) == [6, 5, 1, 4]

    # assert  linkedList.containsNodeWithValue(5), True)


