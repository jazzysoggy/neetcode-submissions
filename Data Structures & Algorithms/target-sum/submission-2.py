class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def backtrack(idx, summed):
            if idx >= len(nums):
                if target == summed:
                    return 1
                else:
                    return 0

            if (idx, summed) in dp:
                return dp[(idx, summed)]

            dp[(idx, summed)] = backtrack(idx + 1, summed + nums[idx]) + backtrack(idx + 1, summed - nums[idx])

            return dp[(idx, summed)]



        return backtrack(0,0)