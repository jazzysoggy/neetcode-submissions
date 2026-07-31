class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def backtrack(perm):
            if len(perm) == len(nums):
                res.add(tuple(perm))
                return


            for i in range(len(nums)):
                if nums[i] == float('-inf'):
                    continue

                number = nums[i]
                nums[i] = float('-inf')
                perm.append(number)
                backtrack(perm)
                nums[i] = number
                perm.pop()

            return

        backtrack([])

        return list(res)
