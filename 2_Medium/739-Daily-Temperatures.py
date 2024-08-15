class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                temppopped, ipopped = stack.pop()
                res[ipopped] = i - ipopped
            stack.append((temp, i))
        return res