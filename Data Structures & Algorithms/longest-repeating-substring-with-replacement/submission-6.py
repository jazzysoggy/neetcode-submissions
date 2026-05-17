class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        track = defaultdict(int)

        l = r = 0

        maxf = 0
        output = 0

        while r < len(s):
            track[s[r]] += 1

            maxf = max(maxf, track[s[r]])

            r += 1

            while (r - l) - maxf > k:
                track[s[l]] -= 1
                l += 1

            output = max(r - l, output)

        return output