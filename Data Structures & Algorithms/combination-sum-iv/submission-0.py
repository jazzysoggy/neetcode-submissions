class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        sorted(nums)

        combinations = defaultdict(int)

        combinations[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                if num > i:
                    continue

                combinations[i] += combinations[i - num]

        return combinations[target]