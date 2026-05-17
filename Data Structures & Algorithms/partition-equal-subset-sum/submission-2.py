class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summed = sum(nums)

        if summed % 2 != 0:
            return False

        selection = [[False] * len(nums) for _ in range(summed // 2 + 1)]
        


        selection[0] = [True] * len(nums)

        for i in range(len(nums)):
            for j in range(nums[i], summed // 2 + 1):
                selection[j][i] = selection[j - nums[i]][i - 1] or selection[j][i - 1]

        return selection[-1][-1]