class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        self.freq = 1

class LinkedList:
    def __init__(self):
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0
    
    def length(self):
        return self.size
    
    def pushRight(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
        self.size += 1
    
    def pop(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev  = prev
        node.prev = None
        node.next = None
        self.size -= 1
    
    def popLeft(self):
        if self.length() == 0:
            return None
        node = self.left.next
        self.pop(node)
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfuCount = 0 # min freq in the cache
        self.nodeMap = {} # key: node
        self.freqMap = defaultdict(LinkedList) # freq: linkedlist

    def counter(self, node):
        # executes when someone calls get/put and updates the data structs
        cnt = node.freq
        self.freqMap[cnt].pop(node)

        if cnt == self.lfuCount and self.freqMap[cnt].length() == 0:
            self.lfuCount += 1
        
        node.freq += 1
        self.freqMap[node.freq].pushRight(node)

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        node = self.nodeMap[key]
        self.counter(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        
        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.val = value
            self.counter(node)
            return
        
        if len(self.nodeMap) == self.cap:
            node = self.freqMap[self.lfuCount].popLeft()
            self.nodeMap.pop(node.key)

        node = ListNode(key, value)
        self.nodeMap[key] = node
        self.freqMap[1].pushRight(node)
        self.lfuCount = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)