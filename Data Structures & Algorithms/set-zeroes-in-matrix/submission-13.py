class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        zeroRow = False
        zeroCol = False

        for i in range(rows):
            zeroRow = zeroRow or matrix[i][0] == 0
            
        for j in range(cols):
            zeroCol = zeroCol or matrix[0][j] == 0

        for i in range(rows - 1, 0, -1):
            for j in range(cols - 1, 0, -1):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if zeroRow:
            for i in range(rows):
                matrix[i][0] = 0

        if zeroCol:
            for j in range(cols):
                matrix[0][j] = 0