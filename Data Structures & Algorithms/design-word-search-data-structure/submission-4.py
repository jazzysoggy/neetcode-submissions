class trie:
    def __init__(self):
        self.next = [None] * 26
        self.word = False

class WordDictionary:

    def __init__(self):
        self.head = trie()

    def addWord(self, word: str) -> None:
        ptr = self.head

        for char in word:
            if not ptr.next[ord(char) - ord('a')]:
                ptr.next[ord(char) - ord('a')] = trie()

            ptr = ptr.next[ord(char) - ord('a')]

        ptr.word = True

    def helper(self, ptr, word, idx):
        if not ptr:
            return False

        if idx >= len(word):
            return ptr.word

        char = ord(word[idx]) - ord('a')

        if word[idx] != '.':
            return self.helper(ptr.next[char], word, idx + 1)
        
        for i in range(26):
            if ptr.next[i] and self.helper(ptr.next[i], word, idx + 1):
                return True

        return False



    def search(self, word: str) -> bool:
        ptr = self.head

        return self.helper(ptr, word, 0)
        
