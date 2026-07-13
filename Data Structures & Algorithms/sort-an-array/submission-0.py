class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 0 or len(nums) == 1:
            return nums

        l = self.sortArray(nums[:len(nums)//2])
        r = self.sortArray(nums[len(nums)//2:])

        output = []

        l1 = 0
        r1 = 0

        while l1 < len(l) or r1 < len(r):
            if r1 >= len(r) or (l1 < len(l) and l[l1] < r[r1]):
                output.append(l[l1])
                l1 += 1
            else:
                output.append(r[r1])
                r1 += 1

        return output
        