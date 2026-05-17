class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        maxLHeight = height[l]
        maxRHeight = height[r]


        output = 0

        while l < r:
            if maxLHeight < maxRHeight:
                output += min(maxLHeight, maxRHeight) - height[l]
                l += 1
                maxLHeight = max(height[l], maxLHeight)
            else:
                output += min(maxLHeight, maxRHeight) - height[r]
                r -= 1
                maxRHeight = max(height[r], maxRHeight)


        return output