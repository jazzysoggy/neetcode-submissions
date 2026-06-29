class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(s, l, r):
            if l >= r:
                return True

            if s[l] != s[r]:
                return False

            return checkPalindrome(s, l + 1, r - 1)

        l,r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return (checkPalindrome(s, l + 1, r) or
                        checkPalindrome(s, l, r - 1))
            l += 1
            r -= 1

        return True