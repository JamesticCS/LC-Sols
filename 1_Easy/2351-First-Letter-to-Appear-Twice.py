class Solution:
    def repeatedCharacter(self, s: str) -> str:

        charset = set()

        for c in s:
            if c in charset:
                return c
            else:
                charset.add(c)
                
        