class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def wordSearch(i, j, idx, tracked):
            nonlocal board
            nonlocal word

            if idx >= len(word):
                return True

            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return False

            if board[i][j] != word[idx]:
                return False
            
            if (i,j) in tracked:
                return False

            tracked[(i,j)] = True

            if wordSearch(i+1,j,idx+1,tracked):
                return True
            
            if wordSearch(i-1,j,idx+1,tracked):
                return True
            
            if wordSearch(i,j+1,idx+1,tracked):
                return True

            if wordSearch(i,j-1,idx+1,tracked):
                return True

            del tracked[(i,j)]
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if wordSearch(i,j,0,{}):
                    return True

        return False    