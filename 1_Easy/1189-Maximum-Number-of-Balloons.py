class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        countArr = [0,0,0,0,0] #count for letters b, a, l, o, n
        
        for c in text:
            if c == 'b':
                countArr[0] += 1
            elif c == 'a':
                countArr[1] += 1
            elif c == 'l':
                countArr[2] += 1
            elif c == 'o':
                countArr[3] += 1
            elif c == 'n':
                countArr[4] += 1
        
        countArr[2] //= 2
        countArr[3] //= 2
        return min(countArr)