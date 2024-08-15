class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        L = 0
        R = len(nums) - 1
        res = []
        while L <= R:
            Lsquared = nums[L] ** 2
            Rsquared = nums[R] ** 2
            if Lsquared >= Rsquared:
                res.append(Lsquared)
                L += 1
            elif Lsquared < Rsquared:
                res.append(Rsquared)
                R -= 1
        return reversed(res)
            