class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # O(n) time, O(n) space
        charset = set()
        L = 0
        maxcount = 0

        for R in range(len(s)):
            while s[R] in charset:
                charset.remove(s[L])
                L += 1
            charset.add(s[R])
            maxcount = max(maxcount, R - L + 1)
        return maxcount