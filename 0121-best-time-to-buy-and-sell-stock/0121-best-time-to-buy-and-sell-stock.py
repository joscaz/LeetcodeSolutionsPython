class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]
        for sell in prices[1:]:
            max_profit = max(max_profit, sell - buy)
            if buy > sell:
                buy = sell

        return max_profit