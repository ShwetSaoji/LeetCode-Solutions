class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = -1
        buy = prices[0]

        for i in prices:
            if i < buy:
                buy = i
            maxprofit = max(maxprofit, i-buy)
        return maxprofit