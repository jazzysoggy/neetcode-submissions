class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = {}

        if endWord not in wordList:
            return 0
        
        def similar(lhs, rhs):
            if lhs == rhs:
                return False

            difference = False
            
            for i in range(len(lhs)):
                if lhs[i] != rhs[i] and not difference:
                    difference = True
                elif lhs[i] != rhs[i]:
                    return False
            
            return True
        
        queue = deque()

        queue.append((beginWord, 1))

        while len(queue) != 0:
            current = queue.popleft()
            if current[0] == endWord:
                return current[1]
            
            visited[current[0]] = True

            for word in wordList:
                if word in visited:
                    continue
                
                if similar(current[0], word):
                    queue.append((word, current[1] + 1))

        return 0
