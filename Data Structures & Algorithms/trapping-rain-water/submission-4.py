class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = 0
        maxR = 0

        l = 0
        r = len(height) - 1

        output = 0

        while l < r:
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])

            if maxL > maxR:
                output += (maxR - height[r])
                r -= 1
            else:
                output += (maxL - height[l])
                l += 1


        return output