class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        profit = 0
        while r < len(prices):
            #Loss
            if prices[r] < prices[l]:
                l = r    
            #profit
            else:
                profit = max(profit, prices[r] - prices[l])
                r += 1
        return profit