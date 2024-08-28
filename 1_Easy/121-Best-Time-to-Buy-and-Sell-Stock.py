class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0
        minprice = prices[0]
        maxprice = prices[0]

        for price in prices:
            if price > maxprice:
                maxprice = price
            if price < minprice:
                minprice = price
        return maxprice - minprice
