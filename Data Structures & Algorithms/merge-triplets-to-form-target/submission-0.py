class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # can choose 2 different triplets and take the max of each value
        # can do this multiple times
        # goal is to get to target
        # can ignore triplets with any values greater than the target

        # triplet get updated and each turn
        # have a set that tracks whether we have each of the elements in target
        valid = set()

        for t in triplets:
            n1, n2, n3 = t
            if n1 > target[0] or n2 > target[1] or n3 > target[2]:
                continue
            
            for i, v in enumerate(t):
                # we want to now check if the vals at each idx match
                if i not in valid and v == target[i]:
                    valid.add(i)

        return len(valid) == 3