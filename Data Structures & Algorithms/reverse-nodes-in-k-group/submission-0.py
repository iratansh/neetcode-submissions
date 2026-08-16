# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # reverse linked list problem -> reverse a sub portion of the list
        # keep track of the head of the next group while
        # reverse the current group -> link the last node of the current 
        # group to the head of the next group
        def reverse(sublist, k):
            count = 0
            curr = sublist
            prev = None

            while curr and count < k:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                count += 1
            return prev, sublist, curr 

        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            # check there are k nodes ahead
            kth = groupPrev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            groupStart = groupPrev.next
            newHead, newTail, nextStart = reverse(groupStart, k)

            # stitch
            groupPrev.next = newHead
            newTail.next = nextStart

            # advance
            groupPrev = newTail






        

            

