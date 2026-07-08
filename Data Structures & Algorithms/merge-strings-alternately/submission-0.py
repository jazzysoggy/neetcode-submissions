class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = 0
        l2 = 0
        newStr = ""

        while l1 < len(word1) and l2 < len(word2):
            newStr += word1[l1] + word2[l2]

            l1 += 1
            l2 += 1

        newStr += word1[l1:] + word2[l2:]

        return newStr