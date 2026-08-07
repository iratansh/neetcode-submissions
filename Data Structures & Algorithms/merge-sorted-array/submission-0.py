class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        i, j = m - 1, n - 1 # end of nums1 (valid), end of num2s

        while j >= 0 :
            if i >= 0 and nums1[i] > nums2[j]: # move nums1[i] to the last element in nums1
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1
            
            last -= 1

