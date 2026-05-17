# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head

        minusN = current
        prevMinusN = None

        while current.next:
            if n <= 1:
                prevMinusN = minusN
                minusN = minusN.next
            else:
                n -= 1

            current = current.next

        if prevMinusN:
            prevMinusN.next = minusN.next

        if minusN == head:
            return head.next

        return head

        