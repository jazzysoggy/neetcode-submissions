class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = 0
        l = 0
        output = 0
        track = defaultdict(int)


        for r in range(len(s)):
            track[s[r]] += 1
            maxf = max(maxf, track[s[r]])

            while r - l + 1 > maxf + k:
                track[s[l]] -= 1
                l += 1
            
            output = max(output, r - l + 1)


        return output