class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1

        while L <= R:
            if not self.isAlphanumeric(s[L]):
                L += 1
                continue
            if not self.isAlphanumeric(s[R]):
                R -= 1
                continue
            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1
        return True
            


    def isAlphanumeric(self, str):
        return  (ord('A') <= ord(str) <= ord('Z')) or (ord('a') <= ord(str) <= ord('z')) or (ord('0') <= ord(str) <= ord('9'))
        