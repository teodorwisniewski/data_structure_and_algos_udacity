



class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


def create_linked_list(list_):
    head = None
    for value in list_:
        if head is None:
            head = Node(value)
            tail = head
        else:
            tail.next = Node(value)
            tail = tail.next
    return head



def read_linked_list(head):
    next_element = head
    while next_element is not None:
        print(next_element.value)
        next_element = next_element.next


if __name__ == "__main__":

    values_for_a_linked_list = [3, 5, 10, 12, 1]
    linked_list = create_linked_list(values_for_a_linked_list)
    read_linked_list(linked_list)