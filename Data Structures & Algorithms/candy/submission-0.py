class Solution:
    def candy(self, ratings: List[int]) -> int:
        # each child gets a candy by default
        # each child is assigned a rating- the rating determines how many candies the child gets in comparison to their neighbors
        # we need to keep track of ratings: ratings[i - 1] and ratings[i + 1]? 
        # candies[i] = max(candies[i - 1], candies[i + 1]) + 1
        n = len(ratings)
        candies = [1] * n 

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)