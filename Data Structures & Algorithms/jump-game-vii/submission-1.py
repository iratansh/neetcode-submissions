class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # dp[i] is true if i can be reached
        # if destination is a wall, can't reach
        if s[-1] != '0':
            return False

        n = len(s)
        dp = [False] * n
        dp[0] = True
        reachable_count = 0

        for i in range(1, n):
            # 1. Slide in the new element that is now reachable from minJump distance
            if i >= minJump and dp[i - minJump]:
                reachable_count += 1
            
            # 2. Slide out the element that is now too far away (beyond maxJump)
            if i > maxJump and dp[i - maxJump - 1]:
                reachable_count -= 1

            # 3. Check if current index can be reached
            if s[i] == '0' and reachable_count > 0:
                dp[i] = True

        return dp[n - 1]
            