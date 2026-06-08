# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1

        if list1.val > list2.val:
            return self.mergeTwoLists(list2, list1)
        
        p = ListNode()
        output = p
        p1 = list1
        p2 = list2

        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next

            p = p.next

        p.next = self.mergeTwoLists(p1, p2)

        return output.next