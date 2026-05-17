class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        negMax = [0] * len(nums)
        Max = [0] * len(nums)

        if nums[0] < 0:
            negMax[0] = nums[0]
        
        if nums[0] > 0:
            Max[0] = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > 0:
                Max[i] = nums[i]
                if Max[i-1] > 0:
                    Max[i] *= Max[i-1]
                if negMax[i-1] < 0:
                    negMax[i] = nums[i] * negMax[i-1]
            elif nums[i] < 0:
                negMax[i] = nums[i]
                if Max[i-1] > 0:
                    negMax[i] *= Max[i-1]

                if negMax[i-1] < 0:
                    Max[i] = nums[i] * negMax[i-1]

            else:
                Max[i] = 0
                negMax[i] = 0

        return max(Max)