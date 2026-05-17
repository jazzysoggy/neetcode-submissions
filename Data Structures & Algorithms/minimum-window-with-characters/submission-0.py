class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minSubWin = ""

        track = defaultdict(int)

        for char in t:
            track[char] += 1

        total = len(track)

        l = 0

        for r in range(len(s)):
            track[s[r]] -= 1

            if track[s[r]] == 0:
                total -= 1

            while total <= 0:
                track[s[l]] += 1
                if track[s[l]] > 0:
                    total += 1
                    if r + 1 - l < len(minSubWin) or minSubWin == "":
                        minSubWin = s[l:r + 1]
                l += 1
        
        return minSubWin