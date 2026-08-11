class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        stack = []

        for token in paths:
            if token == "..":
                if stack:
                    stack.pop()
            elif token != "" and token != ".":
                stack.append(token)
            
        
        return "/" + "/".join(stack)