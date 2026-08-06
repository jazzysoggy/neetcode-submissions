class Node:
    def __init__(self):
        self.next = [None] * 26
        self.word = False

class PrefixTree:

    def __init__(self):
        self.prenode = Node()
        self.prenode.word = True

    def insert(self, word: str) -> None:
        ptr = self.prenode

        for char in word:
            idx = ord(char) - ord('a')
            if not ptr.next[idx]:
                ptr.next[idx] = Node()
            
            ptr = ptr.next[idx]
                
        ptr.word = True
            

    def search(self, word: str) -> bool:
        ptr = self.prenode

        for char in word:
            idx = ord(char) - ord('a')
            if not ptr.next[idx]:
                return False
            ptr = ptr.next[idx]

        return ptr.word
        

    def startsWith(self, prefix: str) -> bool:
        ptr = self.prenode

        for char in prefix:
            idx = ord(char) - ord('a')
            if not ptr.next[idx]:
                return False
            ptr = ptr.next[idx]

        return True
        