class Solution:
    def rob(self, nums: List[int]) -> int:
        lastMax = nums[0]
        lastLastMax = 0

        for i in range(1, len(nums)):
            current = max(lastMax, lastLastMax + nums[i])
            lastLastMax = lastMax
            lastMax = current

        return max(lastMax, lastLastMax)