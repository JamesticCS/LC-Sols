class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # O(1) Space complexity (Assuming sorting is O(1) space)
        # O(n^2) time
        res = []
        nums.sort()

        L = 0
        R = len(nums) - 1

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L = i + 1
            R = len(nums) - 1
            while L < R:
                threesum = nums[i] + nums[L] + nums[R]
                if threesum == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1
                    while L < R and nums[L] == nums[L - 1]: # Skip duplicates of L
                        L += 1
                    while L < R and nums[R] == nums[R - 1]:  # Skip duplicates of R
                        R -= 1
                elif threesum > 0:
                    R -= 1
                else:
                    L += 1
                
        return res


        # Solution with O(n) space complexity due to set
        # O(n^2) time
        """
        res = []
        nums.sort()

        L = 0
        R = len(nums) - 1
        tripletset = set()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            L = i + 1
            R = len(nums) - 1
            while L < R:
                threesum = nums[i] + nums[L] + nums[R]
                if threesum == 0:
                    if (nums[i], nums[L], nums[R]) not in tripletset:
                        res.append([nums[i], nums[L], nums[R]])
                        tripletset.add((nums[i], nums[L], nums[R]))
                    else:
                        R -= 1
                        L += 1
                        continue
                elif threesum > 0:
                    R -= 1
                else:
                    L += 1
        return res
        """

