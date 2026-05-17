class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord in wordList:
            return 0

        queue = deque()
        
        current = 0

        queue.append(beginWord)

        wordList = set(wordList)

        def similarWord(word1, word2):
            changes = 0

            for i in range(len(word1)):
                changes += int(word1[i] != word2[i])

            return changes == 1

        while len(queue) > 0:
            current += 1
            for _ in range(len(queue)):
                tracked = queue[0]
                queue.popleft()

                if tracked == endWord:
                    return current

                for word in wordList.copy():
                    if similarWord(tracked, word):


                        queue.append(word)
                        wordList.remove(word)

        return 0