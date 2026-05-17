class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        track_s = defaultdict(int)
        count = 0

        for i in s:
            track_s[i] += 1
            if track_s[i] == 1:
                count += 1

        for j in t:
            track_s[j] -= 1
            if track_s[j] == 0:
                count -= 1
            elif track_s[j] < 0:
                return False

        return count == 0