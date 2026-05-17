class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroVal = -2 ** 32
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][j] = zeroVal


        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == zeroVal:
                    matrix[i][j] = 0
                    for _i in range(len(matrix)):
                        if matrix[_i][j] != zeroVal:
                            matrix[_i][j] = 0
                    for _j in range(len(matrix[0])):
                        if matrix[i][_j] != zeroVal:
                            matrix[i][_j] = 0