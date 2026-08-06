class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]

        while l <= r:
            m = (l + r) // 2

            res = min(nums[m], res)
            print(l, m, r)

            if nums[m] >= nums[l]:
                # 4 5 6 1 2
                # 1 2 3 4 5
                if nums[r] <= nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                # 4 5 6 1 2
                if nums[r] >= nums[m]:
                    r = m - 1
                else:
                    l = m + 1


        return res