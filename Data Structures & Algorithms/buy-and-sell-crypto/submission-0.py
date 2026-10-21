class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        
        for i in range(0,len(prices)-1):
            buy = prices[i]
            for j in prices[i+1:]:
                sell = j
                profit = sell - buy
                total = max(total,profit)

        return total
        