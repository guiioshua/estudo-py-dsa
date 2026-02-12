class Node:
    def __init__(self, value):
        self.value = value
        self.previous_node_ref = None

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, value):
        new_node = Node(value)
        new_node.previous_node_ref = self.head
        self.head = new_node
    
    def pop(self):
        self.head = self.head.previous_node_ref
    
    def peek(self):
        return self.head.value if self.head else None
    
    def is_empty(self):
        return not bool(self.head)


if __name__ == '__main__':    
    stack = Stack()

    print(stack.is_empty())

    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.push(8)
    stack.push(9)
    print(stack.peek())

    stack.pop()
    print(stack.peek())

    print(stack.is_empty())

    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()

    print(stack.is_empty())
    print(stack.peek())