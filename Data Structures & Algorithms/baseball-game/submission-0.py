class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "+":
                n1, n2 = stack[-1], stack[-2]
                stack.append(n1 + n2)
            elif op == "D":
                n1 = stack[-1]
                stack.append(2 * n1)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)