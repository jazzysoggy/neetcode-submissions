class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        outputSum = 0
        def backtrack(i,track):
            nonlocal outputSum
            nonlocal nums

            if i >= len(nums):
                return

            theory = track ^ nums[i]

            outputSum += theory

            backtrack(i + 1, theory) 
            backtrack(i + 1, track) 

        backtrack(0,0)
        return outputSum

        