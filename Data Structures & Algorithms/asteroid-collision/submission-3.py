class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # stack has all the asteroids in postive direction
        stack = []

        for ast in asteroids:
            while stack and stack[-1] > 0 and ast < 0:
                diff = ast + stack[-1]

                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    ast = 0 
                    break
                else:
                    ast = 0
                    stack.pop()
                    break
            if ast:
                stack.append(ast)

        return stack