class Solution:
    def longestPalindrome(self, s: str) -> str:
        def findLongestAtPos(l, r):
            if r >= len(s) or l < 0:
                return (l + 1, r - 1)

            if s[l] != s[r]:
                return (l + 1, r - 1)

            return findLongestAtPos(l - 1, r + 1)

        output = s[0]

        for i in range(len(s) - 1):
            l1, r1 = findLongestAtPos(i, i + 1)
            l2, r2 = findLongestAtPos(i, i)

            l,r = 0,0

            if r1 - l1 > r2 - l2:
                l = l1
                r = r1
            else:
                l = l2
                r = r2

            if len(output) < (r - l + 1):
                output = s[l:r+1]


        return output
