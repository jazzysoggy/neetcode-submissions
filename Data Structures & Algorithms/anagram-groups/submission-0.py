class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []

        dictionary = {}

        for word in strs:
            wordMap = {}
            for char in word:
                wordMap[char] = wordMap.get(char, 0) + 1
            
            wordMap = frozenset(wordMap.items())

            if wordMap not in dictionary:
                dictionary[wordMap] = len(output)
                output.append([])
            
            output[dictionary[wordMap]].append(word)

        return output


            