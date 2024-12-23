class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # brute force O(n^2)
        '''
        for i in range(len(nums)):
            
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]
        return None
        '''

        # O(n)
        hashmap = {}
        for i, num in enumerate(nums):
            if (target - num) in hashmap:
                return [i, hashmap[target-num]]
            hashmap[num] = i

        return None
        