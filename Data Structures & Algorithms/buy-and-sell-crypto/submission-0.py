class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        best_day = prices[0]
        res = 0
        for i in range(1, len(prices)):
            if prices[i] < best_day:
                best_day = prices[i]
            res = max(res, prices[i] - best_day)

        return res