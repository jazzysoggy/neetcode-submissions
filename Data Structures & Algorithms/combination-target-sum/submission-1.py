class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        stack = []

        def backtrack(idx, sumAll):
            nonlocal output
            nonlocal stack
            nonlocal nums
            if sumAll == target and not stack in output:
                output.append(stack.copy())
                return
            if sumAll > target or idx >= len(nums):
                return

            stack.append(nums[idx])
            backtrack(idx, sumAll + nums[idx])
            backtrack(idx + 1, sumAll + nums[idx])
            stack.pop(-1)
            backtrack(idx + 1, sumAll)

        backtrack(0, 0)

        return output