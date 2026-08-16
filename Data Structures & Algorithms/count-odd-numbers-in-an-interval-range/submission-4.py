class Solution:
    def countOdds(self, low: int, high: int) -> int:
        total = high - low + 1
        odds = total // 2

        if total % 2 != 0 and low % 2 != 0:
            odds += 1
        return odds
