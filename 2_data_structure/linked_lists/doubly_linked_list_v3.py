







"""
Doubly linked list exercice
"""
from typing import List, Any


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
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.insertBefore(self.head, node)


    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
        else:
            self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert is self.head and nodeToInsert is self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert is self.head and nodeToInsert is self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.next = node.next
        nodeToInsert.before = node
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        current_node = self.head
        current_position = 1
        while current_node is not None and current_position != position:
            current_node = current_node.next
            current_position += 1
        if current_node is None:
            self.setTail(nodeToInsert)
        else:
            self.insertBefore(current_node, nodeToInsert)


    def removeNodesWithValue(self, value):
        if not self.containsNodeWithValue(value):
            return
        current_node = self.head
        while current_node is not None:
            node_to_remove = node
            node = node.next
            if node_to_remove.value == value:
                self.remove(current_node)

    def remove(self, node):
        if node is self.head:
            self.head = self.head.next
        if node is self.tail:
            self.tail = self.tail.next
        self.remove_node_bindings(node)

    def containsNodeWithValue(self, value):
        current_node = self.head
        while current_node is not None and current_node.value != value:
            current_node = current_node.next
        return current_node is not None

    def remove_node_bindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None



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
    assert linkedList.containsNodeWithValue(5)
    assert linkedList.containsNodeWithValue(4)
    assert linkedList.containsNodeWithValue(1)
    assert not linkedList.containsNodeWithValue(111)

    # linkedList.setHead(five)
    # assert getNodeValuesHeadToTail(linkedList) == [5, 4, 1, 2, 3]
    # assert getNodeValuesTailToHead(linkedList) == [3, 2, 1, 4, 5]

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
    #
    # linkedList.insertAfter(one, three2)
    # assert getNodeValuesHeadToTail(linkedList) == [4, 1, 3, 2, 5, 3, 6]
    # assert getNodeValuesTailToHead(linkedList) == [6, 3, 5, 2, 3, 1, 4]

    linkedList.insertAtPosition(1, three3)
    assert getNodeValuesHeadToTail(linkedList) == [3, 4, 1, 2, 5, 3, 6, 3]
    assert getNodeValuesTailToHead(linkedList) == [3, 6, 3, 5, 2, 1, 4, 3]

    linkedList.insertAtPosition(8, six)
    assert getNodeValuesHeadToTail(linkedList) == [3, 4, 1, 2, 5, 3, 6, 3]
    assert getNodeValuesTailToHead(linkedList) == [3, 4, 1, 2, 5, 3, 6, 3][::-1]

    linkedList.insertAtPosition(8, three3)
    assert getNodeValuesHeadToTail(linkedList) == [4, 1, 2, 5, 3, 6, 3, 3]
    assert getNodeValuesTailToHead(linkedList) == [4, 1, 2, 5, 3, 6, 3, 3][::-1]

    # linkedList.insertAtPosition(3, three3)
    # assert getNodeValuesHeadToTail(linkedList) == [4, 1, 3, 2, 5, 3, 6, 3]
    # assert getNodeValuesTailToHead(linkedList) == [4, 1, 3, 2, 5, 3, 6, 3][::-1]



    linkedList.removeNodesWithValue(3)
    assert getNodeValuesHeadToTail(linkedList) == [4, 1, 2, 5, 6]
    assert getNodeValuesTailToHead(linkedList) == [6, 5, 2, 1, 4]

    linkedList.remove(two)
    assert getNodeValuesHeadToTail(linkedList) == [4, 1, 5, 6]
    assert getNodeValuesTailToHead(linkedList) == [6, 5, 1, 4]

    assert linkedList.containsNodeWithValue(5) is True
    assert linkedList.containsNodeWithValue(9) is False
    assert linkedList.containsNodeWithValue(4) is True
    assert linkedList.containsNodeWithValue(6) is True

    linkedList2 = DoublyLinkedList()
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
    linkedList2.setHead(one)
    assert getNodeValuesHeadToTail(linkedList2) == [1]
    assert getNodeValuesTailToHead(linkedList2) == [1]

    linkedList3 = DoublyLinkedList()
    linkedList3.setTail(one)
    assert getNodeValuesHeadToTail(linkedList3) == [1]
    assert getNodeValuesTailToHead(linkedList3) == [1]

    # Test Case 4
    # {
    #   "nodes": [
    #     {"id": "1", "next": null, "prev": null, "value": 1}
    #   ],
    #   "classMethodsToCall": [
    #     {
    #       "arguments": [1, "1"],
    #       "method": "insertAtPosition"
    #     }
    #   ]
    # }
    node = Node(1)
    linkedList4 = DoublyLinkedList()
    linkedList4.insertAtPosition(1, one)
    assert getNodeValuesHeadToTail(linkedList4) == [1]
    assert getNodeValuesTailToHead(linkedList4) == [1]

    node1 = Node(1)
    node2 = Node(2)
    bindNodes(node1, node2)
    linkedList5 = DoublyLinkedList()
    linkedList5.head = node1
    linkedList5.tail = node2
    assert getNodeValuesHeadToTail(linkedList5) == [1, 2]
    assert getNodeValuesTailToHead(linkedList5) == [2, 1]

    linkedList = DoublyLinkedList()
    one = Node(1)
    two = Node(2)
    three = Node(3)
    three2 = Node(3)
    three3 = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    bindNodes(one, two)
    bindNodes(two, three)
    bindNodes(three, four)
    bindNodes(four, five)
    bindNodes(five, six)
    bindNodes(six, seven)
    linkedList.head = one
    linkedList.tail = seven
    assert getNodeValuesHeadToTail(linkedList) == [1, 2, 3, 4, 5, 6, 7]
    assert getNodeValuesTailToHead(linkedList) == [1, 2, 3, 4, 5, 6, 7][::-1]

    print(len(getNodeValuesTailToHead(linkedList)))
    linkedList.insertAtPosition(7, one)
    assert getNodeValuesHeadToTail(linkedList) == [2, 3, 4, 5, 6, 1, 7]
    assert getNodeValuesTailToHead(linkedList) == [2, 3, 4, 5, 6, 1, 7][::-1]
    assert linkedList.tail.value == 7
    assert linkedList.head.value == 2


    print(len(getNodeValuesTailToHead(linkedList)))
    linkedList.insertAtPosition(1, one)
    assert getNodeValuesHeadToTail(linkedList) == [1, 2, 3, 4, 5, 6, 7]
    assert getNodeValuesTailToHead(linkedList) == [1, 2, 3, 4, 5, 6, 7][::-1]
    assert linkedList.tail.value == 7
    assert linkedList.head.value == 1

    linkedList = DoublyLinkedList()
    one = Node(1)
    linkedList.setHead(one)
    assert getNodeValuesHeadToTail(linkedList) == [1]
    linkedList.remove(one)
    assert getNodeValuesHeadToTail(linkedList) == []












