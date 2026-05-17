class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        trackS = defaultdict(int)
        total = 0
        for i in s:
            trackS[i] += 1
            total += 1
        
        for i in t:
            trackS[i] -= 1
            total -= 1
            if trackS[i] < 0:
                return False

        return total == 0