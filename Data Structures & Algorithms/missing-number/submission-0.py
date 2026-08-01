class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        totalSum = 0

        for i in nums:
            totalSum += i

        n = len(nums) + 1

        expected = int(((n - 1) / 2) * (n))

        print(expected)

        return expected - totalSum