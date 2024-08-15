class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxArea = 0
        L = 0
        R = len(height) - 1

        while L < R:
            currArea = (R-L)* min(height[L], height[R])
            if currArea > maxArea:
                maxArea = currArea
            if height[L] > height[R]:
                R -= 1
            else:
                L += 1       
        return maxArea     