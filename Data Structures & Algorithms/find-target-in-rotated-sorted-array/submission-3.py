class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1


        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:
                # 3 4 5 6 7
                if target < nums[l] or nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            else:
                # 4 5 1 2 3
                if target <= nums[r] and nums[m] <= target:
                    l = m + 1
                else:
                    # target > nums[r] or nums[m] > target
                    r = m - 1



        return -1