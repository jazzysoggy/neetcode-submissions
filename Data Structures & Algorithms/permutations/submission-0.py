class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        stack = nums

        def backtrack(idx):
            nonlocal nums
            nonlocal stack
            nonlocal output
            if idx >= len(nums) - 1:
                output.append(stack.copy())
                return

            for i in range(idx, len(nums)):
                stack[idx], stack[i] = stack[i], stack[idx]
                backtrack(idx + 1)
                stack[idx], stack[i] = stack[i], stack[idx]

        backtrack(0)

        return output