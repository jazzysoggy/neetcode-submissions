class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        track_allowed = [False] * (len(s) + 1)
        track_allowed[0] = True

        for i in range(1, len(s) + 1):
            for word in wordDict:
                if i >= len(word) and track_allowed[i - len(word)] == True and s[i - len(word):i] == word:
                    track_allowed[i] = True
                    break



        return track_allowed[-1]

        