class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        best = 0
        curr_tank = 0
        for i in range(len(gas)):
            curr_tank += gas[i] - cost[i]

            if curr_tank < 0:
                best = i + 1
                curr_tank = 0
                continue
        return best