class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        char_count_s = {}
        char_count_t = {}

        for char in s:
            char_count_s[char] = char_count_s.get(char, 0) + 1

        for char in t:
            char_count_t[char] = char_count_t.get(char, 0) + 1

        return char_count_s == char_count_t