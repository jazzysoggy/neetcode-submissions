class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0
        i = 1

        while i < len(s):
            prev = s[i - 1]
            curr = s[i]

            if prev == 'I' and curr == 'V':
                output += 4
                i += 2
            elif prev == 'I' and curr == 'X':
                output += 9
                i += 2
            elif prev == 'X' and curr == 'L':
                output += 40
                i += 2
            elif prev == 'X' and curr == 'C':
                output += 90
                i += 2
            elif prev == 'C' and curr == 'D':
                output += 400
                i += 2
            elif prev == 'C' and curr == 'M':
                output += 900
                i += 2
            else:
                if prev == 'I':
                    output += 1
                elif prev == 'V':
                    output += 5
                elif prev == 'X':
                    output += 10
                elif prev == 'L':
                    output += 50
                elif prev == 'C':
                    output += 100
                elif prev == 'D':
                    output += 500
                elif prev == 'M':
                    output += 1000
                i += 1
        if i - 1 < len(s):
            prev = s[i - 1]
            if prev == 'I':
                output += 1
            elif prev == 'V':
                output += 5
            elif prev == 'X':
                output += 10
            elif prev == 'L':
                output += 50
            elif prev == 'C':
                output += 100
            elif prev == 'D':
                output += 500
            elif prev == 'M':
                output += 1000

        return output