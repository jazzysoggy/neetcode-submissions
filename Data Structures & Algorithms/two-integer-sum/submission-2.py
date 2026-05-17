class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        kMinusNum = defaultdict(list)

        for i in range(len(nums)):
            kMinusNum[target - nums[i]].append(i)

        for i in range(len(nums)):
            if nums[i] == target // 2 and len(kMinusNum[nums[i]]) > 1:
                return sorted([i, kMinusNum[nums[i]][1]])
            elif nums[i] != target // 2 and len(kMinusNum[nums[i]]) > 0:
                return sorted([i, kMinusNum[nums[i]][0]])

        return [0,0]