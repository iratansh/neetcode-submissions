class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # must use constanct space
        # find indexes of two nums that sum to target
        # since array is sorted we can use 2 pointers to find the indexes that sum to target
        # can use binary search to narrow down the search space?
        l, r = 0, len(numbers) - 1
        while l < r:
            currSum = numbers[l] + numbers[r]

            if currSum == target:
                return [l + 1, r + 1]

            if currSum > target:
                r -= 1
            else:
                l += 1
        
            