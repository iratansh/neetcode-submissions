class TimeMap:

    def __init__(self):
        # hashmap + BS -> key: List[(timestamp, value)] this ensures that the list is always in sorted order by timestamp
        # we want to conduct a BS on the list to find the corresponding value at timestamp
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # conduct BS on the key list
        # returns the prev timestamp closest to timestamp 
        arr = self.store[key]
        l, r = 0, len(arr) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2

            if arr[mid][0] == timestamp:
                return arr[mid][1]
            
            if arr[mid][0] < timestamp:
                res = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res
