class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxCurr = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            maxCurr = max(nums[i], maxCurr + nums[i])
            res = max(maxCurr, res)
        return res
