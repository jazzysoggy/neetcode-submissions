# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        compare = head.next

        if not compare:
            return head

        a = head.val
        b = compare.val

        while b != 0:
            a, b = b, a % b

        head.next = ListNode(a, self.insertGreatestCommonDivisors(compare))

        return head
