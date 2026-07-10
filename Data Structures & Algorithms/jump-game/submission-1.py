class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = [False] * len(nums)
        reachable[0] = True

        for i in range(len(nums)):
            for j in range(min(nums[i] + 1, len(reachable) - i)):
                reachable[i + j] = reachable[i + j] or reachable[i]

        return reachable[-1]