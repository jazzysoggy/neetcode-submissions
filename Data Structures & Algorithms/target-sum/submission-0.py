class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        trackSum = 0
        output = 0

        def backtrack(idx):
            nonlocal trackSum
            nonlocal nums
            nonlocal target
            nonlocal output

            if idx >= len(nums):
                if trackSum == target:
                    output += 1
                return

            trackSum += nums[idx]
            backtrack(idx + 1)
            trackSum -= 2 * nums[idx]
            backtrack(idx + 1)
            trackSum += nums[idx]

            
        backtrack(0)

        return output