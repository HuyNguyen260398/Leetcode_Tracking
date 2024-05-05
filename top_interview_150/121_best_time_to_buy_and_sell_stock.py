from ast import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Initialize variables buy with the first element of the prices array and profit as 0.
        # Iterate through the prices starting from the second element.
        # Update the buy variable if the current price is lower than the current buying price.
        # Update the profit if the difference between the current price and the buying price is greater than the current profit.
        # Return the final profit.

        buy = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif (prices[i] - buy) > profit:
                profit = prices[i] - buy

        return profit