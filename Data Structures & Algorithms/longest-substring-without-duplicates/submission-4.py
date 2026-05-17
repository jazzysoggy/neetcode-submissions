class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        mapping = {}
        maxLength = 0

        while right < len(s):

            if s[right] in mapping:
                while s[right] in mapping:
                    del mapping[s[left]]
                    left += 1

            mapping[s[right]] = True
            right += 1
            maxLength = max(maxLength, right - left)

        return maxLength