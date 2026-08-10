class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # keep a counter for s2 to keep track of char and counts
        # iterate through substrings of s1 and check that s2 char counts are satisfied or not- expand or shift the window otherwise
        if len(s1) > len(s2):
            return False
        
        need = Counter(s1)
        window = Counter()
        have = 0
        l = 0

        for r, ch in enumerate(s2):
            window[ch] += 1

            if ch in need and window[ch] == need[ch]:
                have += 1

            # maitain fixed window size == len(s1)
            if r - l + 1 > len(s1):
                left = s2[l]
                if left in need and window[left] == need[left]:
                    have -= 1
                window[left] -= 1
                if window[left] == 0:
                    del window[left]
                l += 1
            if have == len(need):
                return True
        return False
