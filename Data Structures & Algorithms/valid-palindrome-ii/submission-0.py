class Solution:
    def validPalindrome(self, s: str) -> bool:
        # i guess the idea would be to have a pointer at the beginning of the string and a pointer at the end of the string
        # and then bascially skip the first different char and then see if the rest of the string forms a palindrome now
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # This is your "one chance"
                # if the 2 chars arent equal we can either skip the char on the l and check if the rest of the string is a palindrome or skip the char on the right and check if the string is a palindrome
                return is_palindrome(l + 1, r) or is_palindrome(l, r - 1)
            l += 1
            r -= 1
        
        return True
        