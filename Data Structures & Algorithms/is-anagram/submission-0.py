class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictCount1 = {}
        dictCount2 = {}

        for char in s:
            dictCount1[char] = dictCount1.get(char, 0) + 1

        for char in t:
            dictCount2[char] = dictCount2.get(char, 0) + 1
        
        for key in dictCount1:
            if key not in dictCount2 or dictCount1[key] != dictCount2[key]:
                return False

        for key in dictCount2:
            if key not in dictCount1 or dictCount1[key] != dictCount2[key]:
                return False  

        return True
            