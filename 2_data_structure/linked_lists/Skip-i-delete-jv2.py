"""
Problem Statement
You are given the head of a linked list and two integers, i and j.
You have to retain the first i nodes and then delete the next j nodes.
 Continue doing so until the end of the linked list.

Example:

linked-list = 1      2      3 4 5        6 7 8 9 10 11 12
i = 2
j = 3
Output = 1 2 6 7 11 12
"""



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



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
        print(head.data, end=' ')
        head = head.next
    print()


def test_function(test_case):
    head = test_case[0]
    i = test_case[1]
    j = test_case[2]
    solution = test_case[3]

    temp = skip_i_delete_j(head, i, j)
    index = 0
    try:
        while temp is not None:
            if temp.data != solution[index]:
                print(" \n\nFail \n\n")
                return
            index += 1
            temp = temp.next
        print("\n\n Pass \n\n")
    except Exception as e:
        print("\n\n Fail \n\n")


def skip_i_delete_j(head, i, j):
    """
    :param: head - head of linked list
    :param: i - first `i` nodes that are to be skipped
    :param: j - next `j` nodes that are to be deleted
    return - return the updated head of the linked list
    """

    if i == 0:
        return None

    current_node = head

    while current_node is not None:
        if current_node is not head:
            last_to_keep.next = current_node

        for _ in range(i):
            if current_node is None:
                break
            print(f"Keep this node {current_node.data}")
            last_to_keep = current_node
            current_node = current_node.next

        for _ in range(j):
            if current_node is None:
                break
            print(f"Remove this node {current_node.data}")
            current_node = current_node.next
    last_to_keep.next = None
    return head




if __name__ == "__main__":

    arr = [1, 2,     3, 4,   5, 6,   7, 8,    9, 10,   11, 12]
    i = 2
    j = 2
    head = create_linked_list(arr)
    solution = [1, 2, 5, 6, 9, 10]
    # check = skip_i_delete_j(head, i, j)
    # print_linked_list(check)
    test_case = [head, i, j, solution]
    test_function(test_case)

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    i = 2
    j = 3
    head = create_linked_list(arr)
    solution = [1, 2, 6, 7, 11, 12]
    test_case = [head, i, j, solution]
    test_function(test_case)

    arr = [1, 2, 3, 4, 5]
    i = 2
    j = 4
    head = create_linked_list(arr)
    solution = [1, 2]
    test_case = [head, i, j, solution]
    test_function(test_case)

    arr = [1, 2, 3, 4, 5]
    i = 2
    j = 0
    head = create_linked_list(arr)
    solution = [1, 2, 3, 4, 5]
    test_case = [head, i, j, solution]
    test_function(test_case)