class Solution:
    def isHappy(self, n: int) -> bool:
        
        fast = n
        slow = n

        def helper(n):
            output = 0
            while n > 0:
                output += (n % 10) * (n % 10)
                n = n // 10
            return output

        while fast != 1 and slow != 1:
            slow = helper(slow)
            fast = helper(helper(fast))
            if fast == slow and fast != 1:
                return False

        return True