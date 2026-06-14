class Solution:
    def countSubstrings(self, s: str) -> int:
        output = 0
        def helper(s, l, r):
            output = 0
            if l < 0 or r >= len(s) or s[l] != s[r]:
                return 0

            return 1 + helper(s, l-1, r+1)

        for i in range(len(s)):
            output += helper(s, i, i)
            output += helper(s, i, i + 1)

        return output