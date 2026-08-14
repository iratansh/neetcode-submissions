# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        tail = dummy

        for _ in range(n + 1):
            tail = tail.next
        
        # now dummy is at the n - 1th node
        # can walk tail forward till it reaches the end of the list and curr should be 
        # curr before the node to delete
        curr = dummy
        while tail:
            tail = tail.next
            curr = curr.next

        curr.next = curr.next.next
        return dummy.next