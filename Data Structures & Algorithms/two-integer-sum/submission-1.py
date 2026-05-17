class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        trackIdx = {}
        for i in range(len(nums)):
            trackIdx[target - nums[i]] = i

        for i in range(len(nums)):
            if nums[i] in trackIdx and i != trackIdx[nums[i]]:
                return [i, trackIdx[nums[i]]]

        