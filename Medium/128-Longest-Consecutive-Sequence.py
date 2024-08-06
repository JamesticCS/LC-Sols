class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        numset = set(nums)
        maxcount = 0
        currcount = 0
        for num in numset:
            currnum = num
            if currnum - 1 not in numset:
                currcount = 1
                while True:
                    if currnum + 1 in numset:
                        currcount += 1
                        currnum += 1
                    else:
                        if currcount > maxcount:
                            maxcount = currcount
                        break
        return maxcount

                




        