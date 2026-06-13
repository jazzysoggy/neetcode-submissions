class Solution:
    def helper(self, n: int, reachedNum: dict) -> bool:
        if n == 1:
            return True

        output = 0
        while n != 0:
            square = n % 10
            output += square * square

            n = n // 10

        if output in reachedNum:
            return False

        reachedNum[output] = True

        return self.helper(output, reachedNum)

    def isHappy(self, n: int) -> bool:
        return self.helper(n, {})
            