class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        stack = []

        def subset(idx):
            if (idx >= len(nums)):
                return
                
            stack.append(nums[idx])
            res.append(stack.copy())
            subset(idx + 1)
            stack.pop()
            subset(idx + 1)

        subset(0)

        return res