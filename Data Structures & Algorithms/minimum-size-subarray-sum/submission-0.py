class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float("inf")
        l = 0
        window = Counter()
        curr_sum = 0

        for r in range(len(nums)):
            window[nums[r]] += 1
            curr_sum += nums[r]

            while curr_sum >= target:
                window[nums[l]] -= 1
                if window[nums[l]] == 0:
                    del window[nums[l]]
                curr_sum -= nums[l]
                min_len = min(min_len, r - l + 1)
                l += 1
        return min_len if min_len < float("inf") else 0