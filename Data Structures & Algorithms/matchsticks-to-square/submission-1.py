class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # square has 4 equal sides meaning we need to partition the matches into 4 subarrays such that 
        # the sum of each subarray's are equal?
        if sum(matchsticks) % 4 != 0: return False
        targ = sum(matchsticks) // 4
        matchsticks.sort(reverse=True)
        
        for match in matchsticks:
            if match > targ: return False

        sides = [0, 0, 0, 0]
        def backtrack(i):
            if i == len(matchsticks):
                # check if all 4 sides are equal
                sideA = sides[0]
                for side in sides:
                    if side != sideA:
                        return False
                    return True
            
            for j in range(len(sides)): # try places matchsticks[i] into each position of sides[j]
                if sides[j] + matchsticks[i] > targ:
                    continue
                
                sides[j] += matchsticks[i]
                if backtrack(i + 1):
                    return True
                sides[j] -= matchsticks[i]
            return False
            
        return backtrack(0)