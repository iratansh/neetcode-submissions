class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        heap = [] # (val, id, node) min heap
        id = 0
        dummy = ListNode()
        tail = dummy

        for lst in lists:
            heapq.heappush(heap, (lst.val, id, lst)) # val, id, node
            id += 1
        
        while heap:
            _, _, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(heap, (node.next.val, id, node.next))
                id += 1


        return dummy.next