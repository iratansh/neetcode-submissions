class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        n = len(nums)
        threshold = n // 3
        res = []

        for key, val in count.items():
            if val > threshold:
                res.append(key)
        return res