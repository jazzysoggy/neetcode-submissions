class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 0:
            return [1]

        digits[-1] = digits[-1] + 1

        if digits[-1] >= 10:
            digits = self.plusOne(digits[:-1]) + [digits[-1] % 10]

        return digits
        

        