class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        
        track = defaultdict(int)

        output = 0

        for right in range(len(s)):
            track[s[right]] += 1

            while track[s[right]] > 1 and left < right:
                track[s[left]] -= 1
                left += 1

            output = max(output, right - left + 1)

        return output