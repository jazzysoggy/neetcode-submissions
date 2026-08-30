class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        output = [0] * (len(s) + 1)

        for i in range(1, len(s) + 1):
            output[i] = output[i - 1] + 1
            for string in dictionary:
                if len(string) > i:
                    continue

                if s[i - len(string):i] != string:
                    continue

                output[i] = min(output[i], output[i - len(string)])

        return output[-1]