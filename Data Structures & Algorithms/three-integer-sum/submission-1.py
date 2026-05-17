class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nextNum = {}

        nums.sort()

        for i in range(len(nums)):
            nextNum[nums[i]] = i

        l = r = 0

        output = []

        while l < len(nums):
            r = l + 1
            while r < len(nums):
                target = - nums[l] - nums[r]
                if target in nextNum and nextNum[target] > l and nextNum[target] > r:
                    output.append([nums[l], nums[r], nums[nextNum[target]]])
                r = nextNum[nums[r]] + 1

            l = nextNum[nums[l]] + 1

        return output