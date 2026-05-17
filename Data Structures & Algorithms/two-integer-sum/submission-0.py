class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}

        for i in range(len(nums)):
            mapping[target-nums[i]] = i
        
        for i in range(len(nums)):
            if nums[i] in mapping and i != mapping[nums[i]]:
                return [i, mapping[nums[i]]] if i < mapping[nums[i]] else [mapping[nums[i]], i]

        return [-1,-1]