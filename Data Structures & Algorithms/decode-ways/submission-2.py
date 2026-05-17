class Solution:
    def numDecodings(self, s: str) -> int:
        counts = [0] * (len(s) + 1)

        counts[0] = 1


        for i in range(len(s)):
            if s[i] != '0':
                counts[i + 1] += counts[i]

            if i > 0 and s[i - 1] != '0' and s[i - 1] <= '2' and (s[i - 1] != '2' or s[i] in '0123456'):
                counts[i + 1] += counts[i - 1]

        return counts[-1]
