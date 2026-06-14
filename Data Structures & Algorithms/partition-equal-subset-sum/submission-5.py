class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        targetNum = sum(nums)

        if targetNum % 2 != 0:
            return False

        targetNum = targetNum // 2

        arraySum = [False for _ in range(targetNum + 1)]

        arraySum[0] = True

        for i in range(len(nums)):

            for j in range(targetNum, nums[i] - 1, -1):
                arraySum[j] = arraySum[j] or arraySum[j - nums[i]]

        return arraySum[-1]
        