# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryNumber = 0
        output = ListNode()
        ptr = output

        while l1 and l2:
            ptr.next = ListNode((l1.val + l2.val + carryNumber) % 10)

            carryNumber = (l1.val + l2.val + carryNumber) // 10
            ptr = ptr.next
            l1 = l1.next
            l2 = l2.next


        while l1:
            ptr.next = ListNode((l1.val + carryNumber) % 10)

            carryNumber = (l1.val + carryNumber) // 10
            ptr = ptr.next
            l1 = l1.next


        while l2:
            ptr.next = ListNode((l2.val + carryNumber) % 10)

            carryNumber = (l2.val + carryNumber) // 10
            ptr = ptr.next
            l2 = l2.next


        while carryNumber != 0:
            ptr.next = ListNode((carryNumber) % 10)

            ptr = ptr.next

            carryNumber = (carryNumber) // 10

        return output.next
        