# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # move p1 up left nodes & p2 up right nodes
        # then conduct a reversal for p1 - p2
        # keep the pointers of the node before p1 and after p2 so we can reconnect the list after reversal
        if not head or left == right:
            return head
        
        dummy = ListNode(0, head)
        left_prev = dummy

        # move left_prev forward until its at left - 1
        for _ in range(left - 1):
            left_prev = left_prev.next
        
        # reverse sublist from left to right
        curr = left_prev.next
        prev = None
        
        # right - left + 1 nodes get reversed
        for _ in range(right - left + 1):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        # curr is now 
        left_prev.next.next = curr
        left_prev.next = prev

        return dummy.next
        
        
        