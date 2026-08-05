class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 0:
            return 0
        def rob_test(offset):
            rob_one = 0
            rob_two = 0

            for i in range(offset, len(nums) + offset - 1):
                curr = max(rob_two + nums[i], rob_one)

                rob_one, rob_two = curr, rob_one

            return max(rob_one, rob_two)

        output = max(rob_test(0), rob_test(1))

        return output