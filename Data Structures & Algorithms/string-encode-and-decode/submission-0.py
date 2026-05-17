class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""

        for i in strs:
            output += str(len(i))
            output += "/"
            output += i

        return output


    def decode(self, s: str) -> List[str]:
        output = []

        while len(s) > 0:
            tokens = s.split('/', 1)
            count = int(tokens[0])
            output.append(tokens[1][0:count])
            s = tokens[1][count:]

        return output