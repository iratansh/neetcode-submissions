class Solution:
    def decodeString(self, s: str) -> str:
        # use a stack to store the current state of parts we need to extend
        # for instance for heavily nested decodes we need to use the stack to maintain order
        curr_str = ""
        curr_num = 0
        stack = []

        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)
            elif ch == "[":
                stack.append((curr_str, curr_num))
                curr_str, curr_num = "", 0
            elif ch == "]":
                prev_str, prev_num = stack.pop()
                curr_str = prev_str + (prev_num * curr_str)
            else:
                curr_str += ch
        return curr_str