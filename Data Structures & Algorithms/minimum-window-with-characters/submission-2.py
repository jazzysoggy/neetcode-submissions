class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCheck = defaultdict(int)

        nonZero = 0

        for c in t:
            tCheck[(c)] += 1

            if tCheck[(c)] == 1:
                nonZero += 1

        l = 0
        
        minLength = -1
        minInit = 0
        for r in range(len(s)):
            tCheck[s[r]] -= 1
            if tCheck[s[r]] == 0:
                nonZero -= 1

            while nonZero == 0:
                if r + 1 - l < minLength or minLength == -1:
                    minLength = r + 1 - l
                    minInit = l
                tCheck[s[l]] += 1
                if tCheck[s[l]] > 0:
                    nonZero += 1
                l += 1

        return s[minInit:minInit + minLength] if minLength != -1 else ""