class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = Counter()
        need = Counter(t)
        have = 0
        l, best_l, min_len = 0, 0, float("inf")

        for r in range(len(s)):
            char = s[r]
            window[char] += 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == len(need):
                c_l = s[l]
                window[c_l] -= 1
                
                if c_l in need and window[c_l] < need[c_l]:
                    have -= 1
                if window[c_l] == 0:
                    del window[c_l]
                
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    best_l = l

                l += 1

        return s[best_l:best_l + min_len] if min_len < float("inf") else ""