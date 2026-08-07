class trie:
    def __init__(self):
        self.next = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.head = trie()

    def addWord(self, word: str) -> None:
        ptr = self.head

        for char in word:
            if not char in ptr.next:
                ptr.next[char] = trie()

            ptr = ptr.next[char]

        ptr.word = True

    def helper(self, ptr, word, idx):
        if not ptr:
            return False

        if idx >= len(word):
            return ptr.word

        char = word[idx]

        if word[idx] != '.':
            return char in ptr.next and self.helper(ptr.next[char], word, idx + 1)
        
        for i in range(26):
            if chr(ord('a') + i) in ptr.next and self.helper(ptr.next[chr(ord('a') + i)], word, idx + 1):
                return True

        return False



    def search(self, word: str) -> bool:
        ptr = self.head

        return self.helper(ptr, word, 0)
        
