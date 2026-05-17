class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        added = defaultdict(bool)

        output = []
        stack = []

        def backtrack(idx):
            nonlocal output
            nonlocal stack
            nonlocal nums
            if (idx >= len(nums)):
                if not added[tuple(stack)]:
                    added[tuple(stack)] = True
                    output.append(stack.copy())
                return

            backtrack(idx + 1)
            stack.append(nums[idx])
            backtrack(idx + 1)
            stack.pop(-1)

        backtrack(0)

        return output