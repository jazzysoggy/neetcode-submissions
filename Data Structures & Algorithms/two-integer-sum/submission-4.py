class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = {}

        for i in range(len(nums)):
            output[target - nums[i]] = i

        for i in range(len(nums)):
            if nums[i] in output and output[nums[i]] != i:
                return sorted([i, output[nums[i]]])