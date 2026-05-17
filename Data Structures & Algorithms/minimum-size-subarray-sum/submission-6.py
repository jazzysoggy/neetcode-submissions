class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        minLength = 999999999
        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                print(l, r)
                minLength = min(minLength, r - l + 1)
                total -= nums[l]
                l += 1


        return minLength if minLength != 999999999 else 0