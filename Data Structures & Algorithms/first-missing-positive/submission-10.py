class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        output = len(nums) + 1
        for i in range(len(nums)):
            if nums[i] > len(nums):
                continue

            index = abs(nums[i])

            if index <= 0:
                continue

            if nums[index - 1] < 0:
                continue

            if nums[index - 1] == 0:
                nums[index - 1] = -len(nums) + 1
                continue

            nums[index - 1] = -nums[index - 1]

        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1

        return output

