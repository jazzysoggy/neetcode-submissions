class Solution:
    def longestPalindrome(self, s: str) -> str:
        def TestPalin(l, r):
            nonlocal s

            if l < 0 or r >= len(s) or s[l] != s[r]:
                return (l + 1), (r - 1)

            return TestPalin(l - 1, r + 1)

        output = ""
        for i in range(len(s)):
            l_1, r_1 = TestPalin(i, i)
            l_2, r_2 = TestPalin(i, i + 1)
            
            if r_1 - l_1 + 1 > len(output):
                output = s[l_1:r_1 + 1]
            if r_2 - l_2 + 1 > len(output):
                output = s[l_2:r_2 + 1]

        return output