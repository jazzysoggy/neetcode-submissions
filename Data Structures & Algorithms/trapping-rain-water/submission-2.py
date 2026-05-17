class Solution:
    def trap(self, height: List[int]) -> int:
        output = 0
        l = 0
        r = len(height) - 1

        maxL = height[l]
        maxR = height[r]

        while l < r:
            output += maxL - height[l] - height[r] + maxR
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])

        return output

            