class Solution:
    def minWindow(self, s: str, t: str) -> str:
        output = ""


        track = defaultdict(int)

        for char in t:
            track[char] += 1

        counts = len(track)

        left = 0
        for right in range(len(s)):
            char = s[right]
            track[char] -= 1
            if track[char] == 0:
                counts -= 1
                while counts == 0:
                    charL = s[left]
                    track[charL] += 1
                    if track[charL] == 1:
                        counts += 1
                    if len(output) == 0 or right - left < len(output):
                        output = s[left:right + 1]
                    left += 1

        return output