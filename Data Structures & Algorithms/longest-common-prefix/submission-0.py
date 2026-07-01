class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        for i in range(9999):
            tracked = ""
            for string in strs:
                if i >= len(string):
                    return output
                
                if tracked != "" and string[i] != tracked:
                    return output

                tracked = string[i]
            output += tracked

        return output


        