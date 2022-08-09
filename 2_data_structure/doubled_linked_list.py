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
        old_head = self.head
        if node.next is not None or node.prev is not None:
            self.remove(node)

        if old_head is not None:
            self.head = node
            self.head.next = old_head
            old_head.prev = self.head
            self.head.prev = None
        else:
            self.head = node
            self.tail = node

    def setTail(self, node):
        old_tail = self.tail
        if node.next is not None or node.prev is not None:
            self.remove(node)

        if old_tail is not None:
            self.tail = node
            self.tail.next = None
            self.tail.prev = old_tail
            old_tail.next = self.tail
        else:
            self.tail = node
            self.head = node

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert.next is not None or nodeToInsert.prev is not None:
            self.remove(nodeToInsert)
        if node.prev is None:
            self.setHead(nodeToInsert)
        else:
            old_prev = node.prev
            node.prev = nodeToInsert
            nodeToInsert.next = node
            nodeToInsert.prev = old_prev
            old_prev.next = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert.next is not None or nodeToInsert.prev is not None:
            self.remove(nodeToInsert)
        if node.next is None:
            self.setTail(nodeToInsert)
        else:
            old_next = node.next
            node.next = nodeToInsert
            nodeToInsert.next = old_next
            nodeToInsert.prev = node
            old_next.prev = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        flag = False
        if nodeToInsert.next is not None or nodeToInsert.prev is not None:
            flag = True
            self.remove(nodeToInsert)


        counter = 1
        current_node = self.head
        if current_node is None:
            self.setHead(nodeToInsert)
            return
        while current_node.next is not None:
            if counter == position:
                self.insertBefore(current_node, nodeToInsert)
                counter += 1
                break
            else:
                current_node = current_node.next
                counter += 1
        if flag:
            counter += 1
        if counter == position:
            self.setTail()

    def removeNodesWithValue(self, value):
        current_node = self.head
        while current_node.next is not None:
            if current_node.value == value:
                new_current_node = current_node.next
                self.remove(current_node)
                current_node = new_current_node
            else:
                current_node = current_node.next
        if current_node.value == value:
            self.remove(current_node)

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
            self.head = new_head
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
        current_node = self.head
        while current_node.next is not None:
            if current_node.value == value:
                return True
            else:
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
    #
    # linkedList.insertAfter(one, three2)
    # assert getNodeValuesHeadToTail(linkedList) == [4, 1, 3, 2, 5, 3, 6]
    # assert getNodeValuesTailToHead(linkedList) == [6, 3, 5, 2, 3, 1, 4]

    linkedList.insertAtPosition(1, three3)
    assert getNodeValuesHeadToTail(linkedList) == [3, 4, 1, 2, 5, 3, 6, 3]
    assert getNodeValuesTailToHead(linkedList) == [3, 6, 3, 5, 2, 1, 4, 3]

    linkedList.insertAtPosition(8, six)
    assert getNodeValuesHeadToTail(linkedList) == [3, 4, 1, 2, 5, 3, 3, 6]
    assert getNodeValuesTailToHead(linkedList) == [3, 4, 1, 2, 5, 3, 3, 6][::-1]

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
    # assert getNodeValuesTailToHead(linkedList2) == [1]

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









