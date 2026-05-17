class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()

        s = ''.join([char for char in s if char.isalnum()])
        p1 = 0
        p2 = len(s) - 1
        while p1 < p2 and s[p1] == s[p2]:
            p1 += 1
            p2 -= 1

        return p1 >= p2