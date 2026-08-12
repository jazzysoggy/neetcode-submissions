class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []

        currentSolGrid = [['.' for i in range(n)]  for j in range(n)]

        diagTopLeft = defaultdict(bool)

        diagTopRight = defaultdict(bool)

        column = defaultdict(bool)

        def backtrack(i):
            if i == n:
                solutions.append(["".join(row) for row in currentSolGrid])
                return

            for j in range(n):

                if column[j] == True:
                    continue
                
                if diagTopLeft[j+i]:
                    continue

                if diagTopRight[j-i]:
                    continue

                currentSolGrid[i][j] = 'Q'

                column[j] = True
                diagTopLeft[j + i] = True
                diagTopRight[j - i] = True

                backtrack(i + 1)

                column[j] = False
                diagTopLeft[j + i] = False
                diagTopRight[j - i] = False

                currentSolGrid[i][j] = '.'
                    
        backtrack(0)

        return solutions