class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxr = maxprofit = 0

        for p in prices[::-1]:
            maxprofit = max(maxprofit, maxr-p)
            maxr = max(maxr, p)
        
        return maxprofit