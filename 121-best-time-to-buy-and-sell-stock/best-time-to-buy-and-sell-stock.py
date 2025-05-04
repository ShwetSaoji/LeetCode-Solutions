class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        buy = prices[0]

        for i in prices:
            if i < buy:
                buy = i
            profit = max(profit, i-buy)
        
        return profit
