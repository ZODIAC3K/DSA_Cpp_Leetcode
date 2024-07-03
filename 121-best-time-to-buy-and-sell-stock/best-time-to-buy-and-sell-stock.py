class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for p in prices[1:]: # start from 2nd value to end
            if buy_price > p:
                buy_price = p
            profit = max(profit, p - buy_price)
        
        return profit
       
        

        