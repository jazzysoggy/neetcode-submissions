class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        dictionary = {}

        for i in range(len(nums)):
            dictionary[nums[i]] = i
            

        left = 0

        while left < len(nums):
            right = left + 1

            while right < len(nums):
                toFind = 0 - nums[left] - nums[right]

                if toFind in dictionary and dictionary[toFind] > right:
                    output.append([nums[left], nums[right], toFind])

                right = dictionary[nums[right]]  + 1

            left = dictionary[nums[left]]  + 1

        return output
