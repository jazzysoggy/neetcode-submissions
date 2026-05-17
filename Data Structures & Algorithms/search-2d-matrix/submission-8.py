class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix) - 1

        left = 0
        right = len(matrix[0]) - 1

        while top <= bot:
            mid = (top + bot) // 2

            if matrix[mid][left] > target:
                bot = mid - 1
            elif matrix[mid][right] < target:
                top = mid + 1
            else:
                break

        if top > bot:
            return False

        row = (top + bot) // 2

        while left <= right:
            mid = (left + right) // 2

            if matrix[row][mid] > target:
                right = mid - 1
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                return True


        return False