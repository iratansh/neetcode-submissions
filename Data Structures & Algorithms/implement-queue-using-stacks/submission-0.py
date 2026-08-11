class MyQueue:

    def __init__(self):
        # maintain two seperate stacks
        # use the second one as a buffer to maintain FIFO property?
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        # s1 is LIFO therefore need to use s2 to process the elements of s1 in FIFO?
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        # now the elements are in reverse order so we can pop the last element from s2?
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()