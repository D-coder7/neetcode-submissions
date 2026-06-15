class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxr = 0
        maxprofit = 0
        
        for i in range(len(prices)-1, -1, -1):
            maxprofit = max(maxprofit, maxr-prices[i])
            maxr = max(maxr, prices[i])
        
        return maxprofit