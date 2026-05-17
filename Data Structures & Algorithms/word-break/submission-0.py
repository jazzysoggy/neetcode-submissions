class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trackValid = defaultdict(bool)
        trackValid[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if word == s[i:i + len(word)] and trackValid[i + len(word)]:
                    trackValid[i] = True

        return trackValid[0]