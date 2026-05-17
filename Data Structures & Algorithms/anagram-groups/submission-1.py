class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outputs = defaultdict(list)

        for string in strs:
            hashV = [0] * 26

            for char in string:
                hashV[ord(char) - ord('a')] += 1

            outputs[tuple(hashV)].append(string)

        output = []

        for key in outputs:
            output.append(outputs[key])

        return output
            

            