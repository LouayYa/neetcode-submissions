class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxtotal = 0
        minBuy = prices[0]

        for sell in prices:
            maxtotal = max(maxtotal, sell-minBuy)
            minBuy = min(minBuy,sell)
        
        return maxtotal
        