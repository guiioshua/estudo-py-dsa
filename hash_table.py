from sympy import nextprime
from singly_linked_list import LinkedList

class Slot:
    def __init__(self):
        self.chain = LinkedList()
        
    def upsert(self, key, value):
        current = self.chain.head
        while current is not None:
            if current.value[0] == key:
                current.value = (key, value)
                return
            current = current.next_node_ref
        self.chain.append((key, value))

class HashTable:
    def __init__(self, size):
        self.size = nextprime(size)
        self.slots = [Slot() for _ in range(self.size)]
        
    def _get_hash_pos(self, key):
        hashed_key = sum(bytes(key, 'ascii'))
        return hashed_key % self.size    
    
    def put(self, key, value):
        slot_pos = self._get_hash_pos(key)
        self.slots[slot_pos].upsert(key, value)
    
    def get(self, key):
        slot_pos = self._get_hash_pos(key)
        current = self.slots[slot_pos].chain.head
        while current is not None:
            if current.value[0] == key:
                return current.value[1]
            current = current.next_node_ref
        return None
    
    def remove(self, key):
        slot_pos = self._get_hash_pos(key)
        slot = self.slots[slot_pos]
        if not slot or not slot.chain.head:
            return None
        
        chain = slot.chain
        if chain.head.value[0] == key:
            if chain.head == chain.tail:
                chain.tail = None
            chain.head = chain.head.next_node_ref
            return
            
        current = chain.head
        while current.next_node_ref is not None:
            if current.next_node_ref.value[0] == key:
                target = current.next_node_ref
                current.next_node_ref = target.next_node_ref
                if target == chain.tail:
                    chain.tail = current
                return
            current = current.next_node_ref
        
if __name__ == '__main__':
    
    ht = HashTable(1)

    ht.put('key1', 'value1')
    ht.put('box1', 'value2')
    print(ht.get('key1'))
    print(ht.get('box1'))
    ht.remove('key1')
    print(ht.get('key1'))
    print(ht.get('box1'))