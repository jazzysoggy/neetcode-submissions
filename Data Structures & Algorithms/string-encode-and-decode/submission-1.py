class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for string in strs:
            output += str(len(string)) + "\\" + string

        return output

    def decode(self, s: str) -> List[str]:
        output = []
        while len(s) > 0:
            num, s = s.split('\\', 1)

            num = int(num)

            output.append(s[:num])

            s = s[num:]

        return output
