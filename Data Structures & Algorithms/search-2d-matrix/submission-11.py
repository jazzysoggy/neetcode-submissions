class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0
        b = len(matrix) - 1
        picked = -1

        while t <= b:
            m = (t + b) // 2

            if target >= matrix[m][0] and target <= matrix[m][-1]:
                picked = m
                break
            elif target < matrix[m][0]:
                b = m - 1
            else:
                t = m + 1
            

        if picked == -1:
            return False

        l = 0
        r = len(matrix[0])

        while l <= r:
            m = (l + r) // 2

            if target > matrix[picked][m]:
                l = m + 1
            elif target < matrix[picked][m]:
                r = m - 1
            else:
                return True

        return False

