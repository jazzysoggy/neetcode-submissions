class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1

        curr = numbers[p1] + numbers[p2]

        while p1 < p2 and curr != target:
            if curr < target:
                p1 += 1
            else:
                p2 -= 1

            curr = numbers[p1] + numbers[p2]

        return [p1 + 1, p2 + 1]