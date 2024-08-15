class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        # O(mnlog(n))
        for word in strs:
            sorted_word = tuple(sorted(word))
            if sorted_word in hashmap:
                hashmap[sorted_word].append(word)
            else:
                hashmap[sorted_word] = [word]
        
        return list(hashmap.values())