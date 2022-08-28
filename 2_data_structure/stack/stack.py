"""
push - adds an item to the top of the stack
pop - removes an item from the top of the stack (and returns the value of that item)
size - returns the size of the stack
top - returns the value of the item at the top of stack (without removing that item)
is_empty - returns True if the stack is empty and False otherwise
"""

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Stack:

    def __init__(self):

        self.head = None
        self.tail = None
        self.counter = 0

    def push(self, value):
        node = Node(value)
        self.counter += 1
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            temp_prev = self.tail
            self.tail.next = node
            self.tail = node
            self.tail.prev = temp_prev

    def pop(self):
        self.counter -= 1
        if self.head is self.tail:
            node_to_pop = self.head
            self.head = None
            self.tail = None
            return node_to_pop
        else:
            node_to_pop = self.tail
            temp_prev = self.tail.prev
            self.tail.prev = None
            self.tail = temp_prev
            return node_to_pop

    def size(self):
        return self.counter

    def top(self):
        return self.tail.value

    def is_empty(self):
        if self.head is None:
            return True
        return False


if __name__ == "__main__":

    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print(f"The lenght of our stack is {stack.size()}")
    while not stack.is_empty():
        print(f"stack pop {stack.pop().value}")

    print(f"The lenght of our stack is {stack.size()}")
