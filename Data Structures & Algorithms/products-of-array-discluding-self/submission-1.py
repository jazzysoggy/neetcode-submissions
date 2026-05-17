class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        fix = 1

        for i in range(len(nums)):
            output[i] *= fix
            fix *= nums[i]


        fix = 1

        for i in range(len(nums) - 1, -1, -1):
            output[i] *= fix
            fix *= nums[i]

        return output