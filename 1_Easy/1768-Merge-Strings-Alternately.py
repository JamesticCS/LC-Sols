class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        returnstr = ""
        min_length = min(len(word1), len(word2))
        
        for i in range(min_length):
            returnstr += word1[i]
            returnstr += word2[i]
            
        returnstr += word1[min_length:]
        returnstr += word2[min_length:]
        
        return returnstr
