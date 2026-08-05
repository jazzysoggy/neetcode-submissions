class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        output = 0
        is_neg = False
        if x < 0:
            is_neg = True
            x = -x

        bound = 2**31

        while x > 0 and output <= bound:
            output *= 10
            output += x % 10
            x = x // 10

        if is_neg:
            return -output if output <= bound else 0

        return output if output <= bound - 1 else 0

