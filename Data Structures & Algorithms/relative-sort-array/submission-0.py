class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        res = []

        for num in arr2:
            if num in count:
                res.extend([num] * count[num])
                del count[num]
        
        for num in sorted(count.keys()):
            res.extend([num] * count[num])
        return res
        
        
        

