class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""

        for string in strs:
            output += str(len(string)) + "#"
            output += string
        
        return output
    def decode(self, s: str) -> List[str]:
        output = []

        while len(s) > 0:
            length,s = s.split("#", 1)

            output.append(s[:int(length)])

            s = s[int(length):]

        return output 
