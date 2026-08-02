class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        trackChar = defaultdict(int)

        duplicateChar = 0

        l = 0

        output = 0

        for r in range(len(s)):
            trackChar[s[r]] += 1

            if trackChar[s[r]] > 1:
                duplicateChar += 1

            while duplicateChar > 0:
                trackChar[s[l]] -= 1

                if trackChar[s[l]] == 1:
                    duplicateChar -= 1

                l += 1

            output = max(output, r - l + 1)

        return output