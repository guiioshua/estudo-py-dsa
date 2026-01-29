class Node:
    def __init__(self, value):
        self.value = value
        self.next_node_ref = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def read_list(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while current is not self.tail:
            print(f'{current.value}\n| ')
            current = current.next_node_ref
        print(current.value)
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
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

    def _find_predecessor(self, value):
        if self.head is None or self.head.next_node_ref is None:
            return None
        current = self.head
        while current.next_node_ref is not None:
            if current.next_node_ref.value == value:
                return current
            current = current.next_node_ref
        return None
    
    def delete(self, value):
        if self.head is None:
            return
        if self.head.value == value:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next_node_ref
            return

        predecessor = self._find_predecessor(value)        
        if predecessor:
            target = predecessor.next_node_ref
            predecessor.next_node_ref = target.next_node_ref
            if target == self.tail:
                self.tail = predecessor
    
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

for i in range(5, 11):
    lisst.append(i)

lisst.delete(7)

lisst.reverse()

lisst.read_list()