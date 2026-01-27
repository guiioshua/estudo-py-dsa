class Node:
    def __init__(self, value):
        self.value = value
        self.next_node_ref = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def enqueue(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next_node_ref = new_node
            self.tail = new_node
    
    def dequeue(self):
        if self.is_empty():
            return
        self.head = self.head.next_node_ref
        if self.head is None:
            self.tail = None
            
    def front(self):
        return self.head.value if self.head else None
    
    def is_empty(self):
        return not bool(self.head)
    
queue = Queue()

print(queue.is_empty())

queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(8)
queue.enqueue(9)

print(queue.front())
queue.dequeue()
print(queue.front())
queue.dequeue()
print(queue.front())
queue.dequeue()
print(queue.front())
queue.dequeue()
print(queue.front())
queue.dequeue()

print(queue.is_empty())
print(queue.front())