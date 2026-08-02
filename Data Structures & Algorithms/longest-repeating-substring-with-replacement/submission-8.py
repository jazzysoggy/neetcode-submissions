class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)

        maxf = 0

        l = 0

        output = 0

        for r in range(len(s)):
            counter[s[r]] += 1

            maxf = max(maxf, counter[s[r]])

            while (r - l + 1) - maxf > k:
                counter[s[l]] -= 1
                l += 1

            output = max(output, r - l + 1)

        return output