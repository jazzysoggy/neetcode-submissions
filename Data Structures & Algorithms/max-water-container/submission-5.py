class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        output = 0
        while l < r:
            output = max(output, (r - l) * min(heights[r], heights[l]))

            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return output