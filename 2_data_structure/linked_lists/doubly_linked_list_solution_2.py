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
        prev_node = node.prev
        next_node = node.next
        if self.head is None and prev_node is not None or next_node is not None:
            if prev_node is not None and next_node is not None:
                prev_node.next, next_node.prev = next_node, prev_node
            node.next = None
            node.prev = None
        elif prev_node is not None or next_node is not None:
            self.remove(node)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            old_head = self.head
            self.head = node
            self.head.next = old_head
            old_head.prev = self.head


    def setTail(self, node):
        prev_node = node.prev
        next_node = node.next
        if prev_node is not None or next_node is not None:
            self.remove(node)
        if self.tail is None and self.head is None:
            self.setHead(node)
        else:
            old_tail = self.tail
            self.tail = node
            self.tail.prev = old_tail
            old_tail.next = self.tail

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert is node:
            return
        prev_node = nodeToInsert.prev
        next_node = nodeToInsert.next

        if prev_node is not None or next_node is not None:
            self.remove(nodeToInsert)
        if node.prev is None:
            self.setHead(nodeToInsert)
            return
        old_prev = node.prev
        node.prev = nodeToInsert
        nodeToInsert.prev = old_prev
        nodeToInsert.next = node
        old_prev.next = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert is node:
            return
        prev_node = nodeToInsert.prev
        next_node = nodeToInsert.next

        if prev_node is not None or next_node is not None:
            self.remove(nodeToInsert)
        if node.next is None:
            self.setTail(nodeToInsert)
            return
        old_next = node.next
        node.next = nodeToInsert
        nodeToInsert.next = old_next
        nodeToInsert.prev = node
        old_next.prev = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        prev_node = nodeToInsert.prev
        next_node = nodeToInsert.next


        if position == 1:
            self.setHead(nodeToInsert)
            return

        counter = 1
        current_node = self.head
        if current_node is None:
            self.setHead(nodeToInsert)
        while current_node.next is not None:
            if counter == position:
                self.remove(nodeToInsert)
                self.insertBefore(current_node, nodeToInsert)
                return
            current_node = current_node.next
            counter += 1
        if counter == position:
            self.insertBefore(self.tail, nodeToInsert)
            return
        self.setTail(nodeToInsert)


    def removeNodesWithValue(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                node_to_to_remove = current_node
                current_node = current_node.next
                self.remove(node_to_to_remove)
                continue
            current_node = current_node.next



    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        if prev_node is not None and next_node is not None:
            prev_node.next = next_node
            next_node.prev = prev_node
        elif prev_node is None and next_node is not None:
            next_node.prev = None
            self.head = next_node
        elif prev_node is not None and next_node is None:
            prev_node.next = None
            self.tail = prev_node
        else:
            self.head = None
            self.tail = None
        node.prev = None
        node.next = None

    def containsNodeWithValue(self, value:Any) -> bool:

        current_node = self.head
        while current_node.next is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next
        if current_node.value == value:
            return True
        return False




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

    linkedList.insertAtPosition(3, three3)
    assert getNodeValuesHeadToTail(linkedList) == [4, 1, 3, 2, 5, 3, 6, 3]
    assert getNodeValuesTailToHead(linkedList) == [4, 1, 3, 2, 5, 3, 6, 3][::-1]

    # linkedList.insertAtPosition(3, four)
    # assert getNodeValuesHeadToTail(linkedList) == [1, 4, 3, 2, 5, 3, 6, 3]
    # assert getNodeValuesTailToHead(linkedList) == [1, 4, 3, 2, 5, 3, 6, 3][::-1]

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












