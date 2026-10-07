class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        # dp[i][j] represents if the first i chars in s1 and j chars in s2 can interleave to form the first i + j chars of s3
        dp = [[False] * (len(s2) + 1) for _ in range((len(s1) + 1))]
        dp[0][0] = True # two empty strings form an empty s3

        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                # either we can choose s1[i] to go first or s2[j] to go first?
                if i > 0 and (s1[i - 1] == s3[i + j - 1]): # if we choose s1 to go first
                    dp[i][j] = dp[i][j] or dp[i - 1][j] 
                if j > 0 and (s2[j - 1] == s3[i + j - 1]):
                    dp[i][j] = dp[i][j] or dp[i][j - 1] 
        
        return dp[len(s1)][len(s2)]