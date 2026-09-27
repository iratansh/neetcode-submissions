class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n < 2: 
            return n
        
        dp = [[False] * n for _ in range(n)] # stores the number of substrings that are palindromes taking into consideration the chars in s from s[i:j]
        res = 0
        
        for i in range(n):
            dp[i][i] = True
            res += 1

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j] and (dp[i + 1][j - 1] or j - i <= 2):
                    dp[i][j] = True
                    res += 1

        return res
       
                    

