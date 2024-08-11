class Solution:
    def mySqrt(self, x: int) -> int:
        L = 0
        R = x
        if x == 1:
            return 1
        while L <= R:
            mid = (L + R) // 2
            if mid*mid == x:
                return mid
            elif abs(R - L) == 1:
                return L
            elif mid * mid > x:
                R = mid
            else:
                L = mid
        