class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # keep a counter to keep track of the window
        # keep a var keeping track of the max element freq in the window
        window = Counter()
        max_freq = 0
        l = 0
        longest = 0

        for r, char in enumerate(s):
            window[char] += 1
            if window[char] > max_freq:
                max_freq = window[char]

            # while window size - max_freq > k we need to shrink the window
            while (r - l + 1) - max_freq > k:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                
                l += 1
            longest = max(longest, r - l + 1)

        return longest
