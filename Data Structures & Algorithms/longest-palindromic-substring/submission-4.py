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

            if len(output) < (r1 - l1 + 1):
                output = s[l1:r1+1]

            if len(output) < (r2 - l2 + 1):
                output = s[l2:r2+1]

        return output
