# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and slow:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next

            if slow and fast and slow.val == fast.val:
                return True

        return False