class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)

        for string in strs:
            hashed = [0] * 26
            for c in string:
                hashed[ord(c) - ord('a')] += 1

            anagram[tuple(hashed)].append(string)

        output = []
        for key in anagram:
            output.append(anagram[key])

        return output