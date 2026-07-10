class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReachable = 0

        for i in range(len(nums)):
            if maxReachable < i:
                return False

            maxReachable = max(maxReachable, i + nums[i])

        return True