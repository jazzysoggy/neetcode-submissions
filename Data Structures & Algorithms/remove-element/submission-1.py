class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        p = 0

        while p < len(nums):
            if nums[p] == val:
                p += 1
                continue

            nums[i] = nums[p]

            p += 1
            i += 1

        return i