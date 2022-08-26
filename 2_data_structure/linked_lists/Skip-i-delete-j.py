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
    current_node = head
    keep_flag = True
    keep_counter = 0
    remove_flag = False
    remove_counter = 0
    while current_node is not None:
        if keep_flag:
            keep_counter += 1
            print(f"I keep a node with the value {current_node.data}")
            if keep_counter == i:
                keep_flag = False
                remove_flag = True
                last_to_keep = current_node if current_node is not None else None
                print(f"last last_to_keep node with the value {last_to_keep.data}")
                keep_counter = 0
        current_node = current_node.next


        if remove_flag and j != 0:
            remove_counter += 1
            if current_node is not None:
                print(f"I remove a node with the value {current_node.data}")
            if remove_counter == j:
                keep_flag = True
                remove_flag = False
                last_to_keep.next = current_node.next if current_node is not None else None
                if last_to_keep.data is not None and current_node is not None and current_node.next is not None:
                    print(f"last_to_keep {last_to_keep.data} connected to the node {current_node.next.data}")
                remove_counter = 0
                if current_node is not None:
                    current_node = current_node.next

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