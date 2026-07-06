class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        stack = []
        appended = [False] * len(nums)
        output = []
        def dfs():
            nonlocal stack
            nonlocal output
            nonlocal nums
            nonlocal appended

            if len(stack) == len(nums):
                output.append(stack.copy())
                return

            for i in range(len(appended)):
                if not appended[i]:
                    stack.append(nums[i])
                    appended[i] = True
                    dfs()
                    stack.pop(-1)
                    appended[i] = False

        dfs()

        return output