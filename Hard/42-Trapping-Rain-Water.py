class Solution:
    def trap(self, height: List[int]) -> int:

        # O(n) time, O(n) space
        
        maxtoL = [0]*len(height)
        maxtoR = [0]*len(height)
        minofLandR = [0]*len(height)

        maxsofar = 0
        for i in range(len(height)):
            maxtoL[i] = maxsofar
            maxsofar = max(maxsofar, height[i])

        maxsofar = 0
        for i in range(len(height) - 1, -1, -1):
            maxtoR[i] = maxsofar
            maxsofar = max(maxsofar, height[i])

        res = 0
        for i in range(len(height)):
            minofLandR[i] = min(maxtoL[i], maxtoR[i])
            if minofLandR[i] > height[i]:
                res += minofLandR[i] - height[i]
        
        return res
        






                


        

        




        