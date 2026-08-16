class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, r = 0, len(t) - 1
        i = 0

        while l <= r:
            if i == len(s):
                return True
            
            if s[i] == t[l]:
                i += 1
            l += 1
            

        return i == len(s)