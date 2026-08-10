class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        o_to_c = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        # iterate through s. append all open chars to the stack
        for ch in s:
            if ch in o_to_c:
                stack.append(ch)
            else:
                if not stack or o_to_c[stack[-1]] != ch:
                    return False
                stack.pop()
        return not stack