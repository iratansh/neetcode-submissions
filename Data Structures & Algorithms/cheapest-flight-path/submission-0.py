class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst: return 0
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            temp = prices.copy()
            for s, d, p in flights:
                if temp[d] > prices[s] + p:
                    temp[d] = prices[s] + p
            prices = temp
        return prices[dst] if prices[dst] != float("inf") else -1