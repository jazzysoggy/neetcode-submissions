class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(init, fin):
            nonlocal nums
            if (init >= len(nums)):
                return 0
            last = nums[init]
            lastLast = 0
            for i in range(init + 1, fin):
                current = max(last, lastLast + nums[i])
                lastLast = last
                last = current

            return max(last, lastLast)

        return max(helper(1, len(nums)), helper(0, len(nums) - 1))