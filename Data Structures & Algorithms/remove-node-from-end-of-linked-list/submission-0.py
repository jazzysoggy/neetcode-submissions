# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        p0 = None
        p2 = head

        diff = 1

        while p2.next:
            if diff == n:
                p0 = p1
                p1 = p1.next
                diff -= 1
            p2 = p2.next
            diff += 1

        if p0:
            p0.next = p1.next
            return head
        else:
            return head.next
        