class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        foundToSwap = False

        i = 0
        p = 0
        while p < len(nums):
            if p != 0 and nums[p] == nums[p - 1]:
                p += 1
                continue

            nums[i] = nums[p]

            i += 1
            p += 1

        return i