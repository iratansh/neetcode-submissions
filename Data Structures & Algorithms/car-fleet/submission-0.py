class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:  
        # stack keeps track of speeds of fleets?
        # sort pairs in reverse order to process cars closest to the target
        stack = []
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        for p, s in pair:
            time = (target - p) / s
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:# if the new cars time is <= the time before it -> catches up to the prior fleet so merge it
                stack.pop()
            
        return len(stack)
