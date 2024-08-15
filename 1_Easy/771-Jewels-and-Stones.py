class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        jewelsSet = set(jewels)
        jewelsCount = 0
        for c in stones:
            if c in jewelsSet:
                jewelsCount += 1
        return jewelsCount
        