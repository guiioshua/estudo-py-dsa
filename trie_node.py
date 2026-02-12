class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        current_node = self.root
        for letter in word:
            if letter not in current_node.children:
              current_node.children[letter] = TrieNode()
            current_node = current_node.children[letter]
        current_node.isEnd = True

    def search(self, word):
        current_node = self.root
        for letter in word:
            if letter not in current_node.children:
                return False
            current_node = current_node.children[letter]
        return True if current_node.isEnd else False
    
    def contains(self, prefix):
        current_node = self.root
        for letter in prefix:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                return False
        return True


if __name__ == '__main__':    
    trie = Trie()


    trie.insert('bananaa')
    trie.insert('maçã')
    trie.insert('pera')

    print(trie.contains('ban'))
    print(trie.search('banana'))
    print(trie.search('pe'))
    print(trie.search('maçana'))