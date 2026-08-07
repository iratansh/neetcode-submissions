class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        threshold = len(nums) // 2

        for key, val in count.items():
            if val > threshold:
                return key
            