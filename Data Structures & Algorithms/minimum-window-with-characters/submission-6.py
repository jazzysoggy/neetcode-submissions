class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required = defaultdict(int)

        active = 0

        for char in t:
            required[char] += 1

            if required[char] == 1:
                active += 1

        l = 0
        output = [0,-1]

        for r in range(len(s)):
            required[s[r]] -= 1

            if required[s[r]] == 0:
                active -= 1

            print(s[r], active)

            while active == 0 and l <= r:
                if output[1] - output[0] > r - l or output[1] - output[0] < 0:
                    print(output)
                    output = [l,r]

                required[s[l]] += 1
                l += 1

                if required[s[l - 1]] == 1:
                    active += 1
                    break

        return s[output[0]:output[1] + 1]