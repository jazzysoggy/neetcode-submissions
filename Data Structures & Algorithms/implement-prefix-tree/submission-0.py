class PrefixTree:

    def __init__(self):
        self.nextLetter = [None] * 26
        self.end = False

    def insert(self, word: str) -> None:
        if len(word) == 0:
            self.end = True
            return
        idx = ord(word[0]) - ord('a')
        if not self.nextLetter[idx]:
            self.nextLetter[idx] = PrefixTree()

        self.nextLetter[idx].insert(word[1::])

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return self.end
        idx = ord(word[0]) - ord('a')
        if not self.nextLetter[idx]:
            return False

        return self.nextLetter[idx].search(word[1::])

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return True
        idx = ord(prefix[0]) - ord('a')
        if not self.nextLetter[idx]:
            return False

        return self.nextLetter[idx].startsWith(prefix[1::])

        