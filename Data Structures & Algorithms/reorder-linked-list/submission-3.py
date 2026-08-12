# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        ptr = slow.next
        prev = slow.next = None
        while ptr:
            next = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = next

        ptr = head
        while prev:
            tmp1, tmp2 = ptr.next, prev.next
            ptr.next = prev
            prev.next = tmp1
            ptr, prev = tmp1, tmp2
    