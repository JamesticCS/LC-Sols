class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ## O(n) time and space 
        hashmap = {')': '(',
                   '}': '{',
                   ']': '['
                   }
        charstack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                charstack.append(char)
            elif not charstack:
                return False
            else:
                if charstack[-1] == hashmap[char]:
                    charstack.pop()
                else:
                    return False
        if charstack == []:
            return True

