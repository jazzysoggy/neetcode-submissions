class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        output = nums[0]
        prefix_sum = nums[0]

        for r in range(1, len(nums)):
            if prefix_sum < 0:
                prefix_sum = 0
                
            prefix_sum += nums[r]
            output = max(output, prefix_sum)

        return output