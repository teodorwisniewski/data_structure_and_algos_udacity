"""
Problem Statement
Given a linked list, swap the two nodes present at position i and j, assuming 0 <= i <= j. The positions are based on 0-based indexing.

Note: You have to swap the nodes and not just the values.

Example:

linked_list = 3 4 5 2 6 1 9
positions = 2 5
output = 3 4 1 2 6 5 9
Explanation:

The node at position 3 has the value 2
The node at position 4 has the value 6
Swapping these nodes will result in a final order of nodes of 3 4 5 6 2 1 9
"""


class Node:
    """LinkedListNode class to be used for this problem"""
    def __init__(self, data):
        self.data = data
        self.next = None


"""
:param: head- head of input linked list
:param: `position_one` - indicates position (index) ONE
:param: `position_two` - indicates position (index) TWO
return: head of updated linked list with nodes swapped

TODO: complete this function and swap nodes present at position_one and position_two
Do not create a new linked list
"""



def test_function(test_case):
    head = test_case[0]
    left_index = test_case[1]
    right_index = test_case[2]

    left_node = None
    right_node = None

    temp = head
    index = 0
    try:
        while temp is not None:
            if index == left_index:
                left_node = temp
            if index == right_index:
                right_node = temp
                break
            index += 1
            temp = temp.next

        updated_head = swap_nodes(head, left_index, right_index)

        temp = updated_head
        index = 0
        pass_status = [False, False]

        while temp is not None:
            if index == left_index:
                pass_status[0] = temp is right_node
            if index == right_index:
                pass_status[1] = temp is left_node

            index += 1
            temp = temp.next

        if pass_status[0] and pass_status[1]:
            print("Pass")
        else:
            print("Fail")
        return updated_head
    except Exception as e:
        print("Fail")


# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()



def swap_nodes(head, left_index, right_index):
    """
    :param: head- head of input linked list
    :param: `position_one` - indicates position (index) ONE
    :param: `position_two` - indicates position (index) TWO
    return: head of updated linked list with nodes swapped

    TODO: complete this function and swap nodes present at position_one and position_two
    Do not create a new linked list
    """
    if head is None:
        return None
    current_node = head
    prev_node = None
    counter = 0
    while current_node is not None:

        if counter == left_index:
            print(f"left node to swap {current_node.data}")
            left_node = current_node
            left_prev = prev_node
            left_next = current_node.next

        if counter == right_index:
            print(f"right node to swap {current_node.data}")
            right_node = current_node
            right_prev = prev_node
            right_next = current_node.next
            break

        prev_node = current_node
        current_node = current_node.next
        counter += 1
    if left_prev is not None and right_next is not None:
        print(f"left_node -> {left_node.data}, left_prev -> {left_prev.data} and left_next -> {left_next.data}")
        print(f"right_node -> {right_node.data}, right_prev -> {right_prev.data} and right_next -> {right_next.data}")

    if left_node is head and left_next is right_node:
        head = right_node
        left_node.next = right_next
        right_node.next = left_node


    elif left_next is right_node:
        left_node.next = right_next
        right_node.next = left_node
        left_prev.next = right_node
    else:
        left_prev.next = right_node
        right_node.next = left_next

        right_prev.next = left_node
        left_node.next = right_next

    return head

if __name__ == "__main__":

    arr = [3, 4, 5, 2, 6, 1, 9]
    head = create_linked_list(arr)
    left_index = 3
    right_index = 4

    test_case = [head, left_index, right_index]
    updated_head = test_function(test_case)

    arr = [3, 4, 5, 2, 6, 1, 9]
    left_index = 2
    right_index = 4
    head = create_linked_list(arr)
    test_case = [head, left_index, right_index]
    updated_head = test_function(test_case)

    arr = [3, 4, 5, 2, 6, 1, 9]
    left_index = 0
    right_index = 1
    head = create_linked_list(arr)
    test_case = [head, left_index, right_index]
    updated_head = test_function(test_case)