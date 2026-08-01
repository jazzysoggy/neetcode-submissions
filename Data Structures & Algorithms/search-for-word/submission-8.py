class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = {}

        def dfs(i, j, idx):
            nonlocal board
            nonlocal word

            if idx >= len(word) - 1:
                return True

            output = False

            visited[(i,j)] = True

            if i > 0 and not (i-1,j) in visited and board[i-1][j] == word[idx + 1]:
                output = output or dfs(i-1,j, idx + 1)

            if j > 0  and not (i,j - 1) in visited and board[i][j - 1] == word[idx + 1]:
                output = output or dfs(i,j - 1, idx + 1)
    
            if i < len(board) - 1  and not (i + 1,j) in visited and board[i+1][j] == word[idx + 1]:
                output = output or dfs(i + 1,j, idx + 1)

            if j < len(board[0]) - 1  and not (i,j + 1) in visited and board[i][j + 1] == word[idx + 1]:
                output = output or dfs(i,j + 1, idx + 1)

            del visited[(i,j)]

            return output

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True


        return False

