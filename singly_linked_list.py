class Node:
    def __init__(self, value):
        self.value = value
        self.next_node_ref = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def read_list(self):
        current = self.head
        while current is not self.tail:
            print(f'{current.value}\n| ')
            current = current.next_node_ref
        print(current.value)
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node_ref = new_node
            self.tail = new_node
    
    def search(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next_node_ref
        return None
    
    def find_last_but_one(self):
        if self.head is None or self.head.next_node_ref is None:
            return None
        current = self.head
        while current.next_node_ref is not self.tail:
            current = current.next_node_ref
        return current

    def delete(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        new_tail = self.find_last_but_one()
        new_tail.next_node_ref = None
        self.tail = new_tail

    def reverse(self):
        current = self.head
        if current is None or current.next_node_ref is None:
            return
        previous = None
        while current is not None:

            next_node = current.next_node_ref
            current.next_node_ref = previous
            previous = current
            current = next_node
        self.tail = self.head
        self.head = previous
        

lisst = LinkedList()

lisst.append(5)
lisst.append(6)
lisst.append(7)
lisst.append(8)
lisst.append(9)
lisst.append(10)

lisst.delete()

lisst.reverse()

lisst.read_list()