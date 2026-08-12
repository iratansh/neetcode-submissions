class FreqStack:

    def __init__(self):
        # self.stack[-1] should store the most frequent element?
        # might need to use a counter along with a stack?
        self.freq = Counter() # val: freq
        self.group = defaultdict(list) # freq: stack of elements for that freq
        self.max_freq = 0 # keep track of max freq to use with self.group

    def push(self, val: int) -> None:
        self.freq[val] += 1
        val_freq = self.freq[val]
        self.group[val_freq].append(val)
        
        if val_freq > self.max_freq:
            self.max_freq = val_freq

    def pop(self) -> int:
        # pop the element with the max_freq
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        if not self.group[self.max_freq]:
            del self.group[self.max_freq]
            self.max_freq -= 1
        return val
  

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()