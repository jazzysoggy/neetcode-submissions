class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        mapping = {}

        for i in range(len(board)):
            mapping["r" + str(i)] = {}
            mapping["c" + str(i)] = {}
        
        for i in range(3):
            for j in range(3):
                mapping[(i,j)] = {}

        for i in range(len(board)):
            for j in range(len(board[0])):
                value = board[i][j]

                if value == ".":
                    continue

                if value in mapping["r" + str(i)]:
                    return False

                mapping["r" + str(i)][value] = True

                if value in mapping["c" + str(j)]:
                    return False
                    
                mapping["c" + str(j)][value] = True

                grid = (i // 3, j // 3)

                if value in mapping[grid]:
                    return False
                    
                mapping[grid][value] = True

        return True



        