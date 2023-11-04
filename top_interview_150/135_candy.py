from ast import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Two Pass approach

        # number of children
        n = len(ratings)

        # list to store number of candies for each child
        candies = [1] * n

        # first pass: check rating from left to right
        for i in range(1, n):
            if ratings[i-1] < ratings[i] and candies[i-1] >= candies[i]:
                candies[i] = candies[i-1] + 1

        # second pass: check rating from right to left
        for i in range(n-2, -1, -1):
            if ratings[i+1] < ratings[i] and candies[i+1] >= candies[i]:
                candies[i] = candies[i+1] + 1

        total_candies = sum(candies)

        return total_candies