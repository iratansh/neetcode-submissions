class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # want to ensure that at least letter appears in at most one substring
        # how can we do the splitting to ensure that this is valid? 
        # we need to keep track of the furthest index seen of each char -> and then we know that the substring needs to be AT LEAST that long to get all of those chars in it
        # however if a substring contains other chars then we also must account for their last position as well? maybe it makes sense to keep track of the furthese position for any char in the current substring
        last = defaultdict(int) # char: furthest index
        for i, el in enumerate(s):
            last[el] = i
        
        res = []
        furthest_i = 0
        curr = []
        
        for i, ch in enumerate(s):
            furthest_i = max(furthest_i, last[ch])
            curr.append(ch)
            
            if i == furthest_i: # then we can append the curr substring to res
                res.append(len(curr))
                curr = []

        return res