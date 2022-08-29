
class Node:

    def __init__(self, data):
        self.value = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.counter = 0

    def size(self):
        return self.counter

    def is_empty(self):
        return self.counter == 0

    def push(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.counter += 1

    def pop(self):
        if self.is_empty():
            return None
        value_to_pop = self.head.value
        self.head = self.head.next

        self.counter -= 1
        return value_to_pop


if __name__ == "__main__":
    # Setup
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)

    # Test size
    print("Pass" if (stack.size() == 5) else "Fail")

    # Test pop
    print("Pass" if (stack.pop() == 50) else "Fail")

    # Test push
    stack.push(60)
    print("Pass" if (stack.pop() == 60) else "Fail")
    print("Pass" if (stack.pop() == 40) else "Fail")
    print("Pass" if (stack.pop() == 30) else "Fail")
    stack.push(50)
    print("Pass" if (stack.size() == 3) else "Fail")