# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pooled = 0

        ptr = ListNode()
        output = ptr

        while l1 and l2:
            pooled += l1.val + l2.val
            l1 = l1.next
            l2 = l2.next

            ptr.next = ListNode(pooled % 10)
            ptr = ptr.next
            pooled = pooled // 10

        while l1:
            pooled += l1.val
            l1 = l1.next

            ptr.next = ListNode(pooled % 10)
            ptr = ptr.next
            pooled = pooled // 10

        while l2:
            pooled += l2.val
            l2 = l2.next

            ptr.next = ListNode(pooled % 10)
            ptr = ptr.next
            pooled = pooled // 10

        while pooled > 0:
            ptr.next = ListNode(pooled % 10)
            ptr = ptr.next
            pooled = pooled // 10
            
        return output.next