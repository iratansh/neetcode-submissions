class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2: 
            return s
        
        # dp[i][j] represents if s[i..j] is a palindrome
        dp = [[False] * n for _ in range(n)]
        longest = 1
        best_l = 0

        for i in range(n):
            dp[i][i] = True # single char strings are palindromes

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j] and (dp[i + 1][j - 1] or j - i <= 2):
                    dp[i][j] = True

                    if j - i + 1 > longest:
                        best_l = i
                        longest = j - i + 1

        return s[best_l:best_l + longest]
        