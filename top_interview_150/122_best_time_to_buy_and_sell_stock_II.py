class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # ==============================================
        # profit = 0

        # for i in range(1, len(prices)):
        #     if prices[i] > prices[i-1]:
        #         profit += prices[i] - prices[i-1]

        # return profit
        # ==============================================

        profit = 0
        start = prices[0]
        days = len(prices)

        for i in range(1, days):
            if prices[i] > start:
                profit += prices[i] - start
            start = prices[i]

        return profit
