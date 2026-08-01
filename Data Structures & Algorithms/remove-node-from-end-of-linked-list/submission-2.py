# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = {}

        head2 = ListNode(-1, head)

        ptr = head2

        length[-1] = ptr

        endVal = 0

        while ptr.next:
            length[endVal] = ptr.next
            endVal += 1
            ptr = ptr.next

        length[endVal - n - 1].next = length[endVal - n].next
        
        return head2.next

        