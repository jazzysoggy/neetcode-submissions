class Solution:
    def rob(self, nums: List[int]) -> int:
        res0 = 0
        res1 = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            temp = res1
            res1 = max(res1, res0 + nums[i])
            res = max(res0, temp, res1)
            res0 = temp

        return res