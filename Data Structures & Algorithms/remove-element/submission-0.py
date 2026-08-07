class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            # If current element is not val, move it to index k
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k