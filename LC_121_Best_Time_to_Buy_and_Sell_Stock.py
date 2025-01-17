class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0  # store profit
        buy_low = prices[0]
        for i in range(1, len(prices)):
            cost = prices[i] - buy_low
            maxProfit = max(maxProfit, cost)
            buy_low = min(buy_low, prices[i])
        return maxProfit
