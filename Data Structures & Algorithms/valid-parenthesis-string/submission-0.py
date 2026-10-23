class Solution:
    def checkValidString(self, s: str) -> bool:
        # have a stack to push open brackets.
        # keep track of the indeixes of unmatched open brackets and also another stack to keep track of star indexes
        # use a star as a backup when matching 
        left = []
        star = []

        for i, ch in enumerate(s):
            if ch == "(":
                left.append(i)
            elif ch == "*":
                star.append(i)
            else: # close brackets
                if not left and not star:
                    return False
                
                if left:
                    left.pop()
                else:
                    star.pop()
        # left may still have values - there are unmatched left brackets left
        while left and star:
            i,j = left.pop(), star.pop()

            # j must be after i to match
            if i > j: return False
        
        # even if star has left over vals they can just be set to ""
        return len(left) == 0


