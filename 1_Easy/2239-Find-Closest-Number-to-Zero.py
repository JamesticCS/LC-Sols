class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        lowest = nums[0]
        for num in nums:
            if abs(num) == abs(lowest):
                lowest = max(num, lowest)
            elif abs(num) < abs(lowest):
                lowest = num
        return lowest

        