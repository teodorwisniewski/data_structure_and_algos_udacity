"""
Sorted singled sorted list where we need to remove duplicates
"""

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_linked_list(list_):

    head = None
    for value in list_:
        if head is None:
            head = LinkedList(value)
            node = head
        else:
            node.next = LinkedList(value)
            node = node.next

    return head

def traverse_linked_list(linked_list):

    if linked_list is None:
        return

    output_values = []
    node = linked_list
    output_values.append(node.value)
    counter = 0
    print(f"{counter + 1}. Node value:{node.value}")
    while node.next is not None:
        node = node.next
        output_values.append(node.value)
        print(f"{counter + 1}. Node value:{node.value}")
        counter += 1
    return output_values


def removeDuplicatesFromLinkedList(linked_list):

    head = linked_list
    node = head
    while node.next is not None:
        if node.value >= node.next.value:
            node.next = node.next.next if node.next.next is not None else None
        else:
            node = node.next
    return head


if __name__ == "__main__":

    values_for_a_linked_list = [1, 1, 3, 4, 5, 5, 6, 6, 6]
    linked_list = create_linked_list(values_for_a_linked_list)
    assert values_for_a_linked_list == traverse_linked_list(linked_list)
    obtained_values = traverse_linked_list(removeDuplicatesFromLinkedList(linked_list))
    expected_values = [1, 3, 4, 5, 6]
    print(obtained_values)
    assert expected_values == obtained_values
