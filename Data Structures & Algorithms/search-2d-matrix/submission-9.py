class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bot = 0
        top = len(matrix) - 1

        left = 0
        right = len(matrix[0]) - 1

        while bot <= top:
            mid = (bot + top) // 2

            if matrix[mid][left] > target:
                top = mid - 1
            elif matrix[mid][right] < target:
                bot = mid + 1
            else:
                break

        if bot > top:
            return False

        median = (bot + top) // 2

        while left <= right:
            mid = (left + right) // 2
            if matrix[median][mid] > target:
                right = mid - 1
            elif matrix[median][mid] < target:
                left = mid + 1
            else:
                return True

        return False