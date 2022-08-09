def getNodeValuesHeadToTail(linkedList):
    values = []
    node = linkedList.head
    while node is not None:
        values.append(node.value)
        node = node.next
    return values


def getNodeValuesTailToHead(linkedList):
    values = []
    node = linkedList.tail
    while node is not None:
        values.append(node.value)
        node = node.prev
    return values


def bindNodes(nodeOne, nodeTwo):
    nodeOne.next = nodeTwo
    nodeTwo.prev = nodeOne




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
        temp = self.tail
        if temp is not None:
            self.tail = node
            self.tail.next = None
            self.tail.prev = temp
        else:
            self.temp = node

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        pass

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        pass

    def insertAtPosition(self, position, nodeToInsert):
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
            self.head = new_head
            node.next = None
            node.prev = None
        elif node.next is not None and node.prev is not None:
            # removing tail
            new_tail = node.prev
            new_tail.next = None
            self.tail = new_tail
            node.next = None
            node.prev = None
        else:
            assert False, "remove It should never happen"


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