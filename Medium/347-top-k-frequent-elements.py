class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashmap = {}
        # O(nlog(n)) (solution not using heap)
        for num in nums:
            if num in hashmap:
                hashmap[num] = hashmap[num] + 1
            else:
                hashmap[num] = 1
        sorted_nums = sorted(hashmap, key=lambda x: hashmap[x], reverse=True)
        return sorted_nums[:k]

        
