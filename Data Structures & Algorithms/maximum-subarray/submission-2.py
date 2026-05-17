class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        output = nums[0]
        for num in nums:
            if curr <= 0:
                curr = 0
            curr += num
            output = max(curr, output)

        return output