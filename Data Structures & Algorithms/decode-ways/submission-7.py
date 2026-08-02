class Solution:
    def numDecodings(self, s: str) -> int:
        array = [0] * (len(s) + 1)

        array[0] = 1

        for i in range(1, len(s) + 1):
            if s[i - 1] != '0':
                array[i] += array[i - 1]

            if i > 1 and ((ord('0') <= ord(s[i - 1]) <= ord('6') and s[i-2] == '2') or (s[i-2] == '1')):
                array[i] += array[i - 2]
        
        return array[-1]