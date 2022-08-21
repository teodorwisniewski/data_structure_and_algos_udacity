




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
    """
    Space complexity Big O(M)
    :param linked_list:
    :return:
    """
    if linked_list is None:
        return LinkedList()

    head = linked_list
    node = head
    counter = 0
    unique_values = set()
    unique_values.add(node.value)
    while node.next is not None:
        if node.next.value in unique_values:
            print(f"{counter + 1}. Node value: {node.next.value} needs to be removed")
            while node.next is not None and node.next.value in unique_values:
                if  node.next.next is not None: print(node.next.value, node.next.next.value)
                node.next = node.next.next

        if node.next is not None and node.next.value not in unique_values:
            unique_values.add(node.next.value)
            node = node.next
            counter += 1

    return head

if __name__ == "__main__":

    values_for_a_linked_list = [3, 5, 5, 3, 3, 7, 0, 0, 0, 1]
    linked_list = create_linked_list(values_for_a_linked_list)
    values = traverse_linked_list(linked_list)
    print(values)
    removed_duplicates = removeDuplicatesFromLinkedList(linked_list)
    values = traverse_linked_list(removed_duplicates)
    print(values)