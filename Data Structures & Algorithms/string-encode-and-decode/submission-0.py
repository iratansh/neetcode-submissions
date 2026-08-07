class Solution:

    def encode(self, strs: List[str]) -> str:
        # encoding pattern follows N#str where N is the length of the string
        res = []
        for string in strs:
            s_len = len(string)
            res.append(str(s_len) + "#" + string)
        return "".join(res)
        
    def decode(self, s: str) -> List[str]:
        # decode the string by doing the reverse
        # we can get the original string by first finding the 
        # integer, continue to iterate nums and build the int 
        # then iterate through N chars following the "#"
        if not s:
            return []
        
        sizes, res, i = [], [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            # now j is at the "#" and i:j is at a number?
            length = int(s[i:j])
            res.append(s[j+1:j+length+1])
            # place i at the element after j
            i = j + length + 1

        return res