class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # have a dict - prefix sum: num ways to reach it
        prefix = defaultdict(int)
        prefix[0] = 1 
        currSum = 0
        res = 0

        for i in range(len(nums)):
            currSum += nums[i]
            if currSum - k in prefix:
                res += prefix[currSum - k]
            prefix[currSum] += 1
        return res
