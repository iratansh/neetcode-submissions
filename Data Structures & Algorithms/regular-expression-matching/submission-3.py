class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j] represents whether p[0...j] matches s[0...i]

        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        # base case: dp[0][0] = True
        dp[0][0] = True

        # dp[0][j] = True if p[0..j] can be set to ""
        for j in range(1, len(p) + 1):
            if j >= 2 and p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]
        
        # main loop
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                # "." case:
                if p[j - 1] == "." or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] 

                # "*" case:
                if j >= 2 and p[j - 1] == "*":
                    # pretend that the star isn't there- look back 2 steps in the pattern
                    dp[i][j] = dp[i][j - 2]

                    # pretend star is there -> match
                    # check if the current char in s matches the preceding element to "*"
                    if p[j - 2] == "." or s[i - 1] == p[j - 2]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                        
        return dp[len(s)][len(p)]