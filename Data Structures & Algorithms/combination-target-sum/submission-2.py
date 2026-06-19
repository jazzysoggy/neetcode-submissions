class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        stack = []

        def helper(idx, sums):
            nonlocal nums
            nonlocal output
            nonlocal stack
            nonlocal target
            if idx == len(nums) or sums > target:
                return

            if sums == target:
                output.append(stack.copy())
                return
                
            stack.append(nums[idx])

            helper(idx, sums + nums[idx])

            stack.pop(-1)

            helper(idx + 1, sums)


        helper(0, 0)
        return output