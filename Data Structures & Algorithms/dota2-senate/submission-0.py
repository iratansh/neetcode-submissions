class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # basically if there are opposers left then the optimal move in the turn is to take their rights 
        # if there are no opposers left -> only then is the optimal move to announce victory
        # we need to keep track of the current positions
        r, d = deque(), deque()
        n = len(senate)

        for i, el in enumerate(senate):
            if el == "R":
                r.append(i)
            else:
                d.append(i)
    

        while r and d:
            dturn = d.popleft()
            rturn = r.popleft()

            if rturn < dturn:
                r.append(rturn + n)
            else:
                d.append(dturn + n)
    

        if r: return "Radiant"
        if d: return "Dire"