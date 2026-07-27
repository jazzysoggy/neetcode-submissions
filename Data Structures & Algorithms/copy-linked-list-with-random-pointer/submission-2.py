"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        trackRandom = {}
        newHead = Node(0)
        ptr = newHead
        ogHead = head

        while head:
            ptr.next = Node(head.val)
            trackRandom[head] = ptr.next

            ptr = ptr.next
            head = head.next

        ptr = newHead.next
        head = ogHead

        while head:
            if head.random:
                ptr.random = trackRandom[head.random]

            head = head.next
            ptr = ptr.next


        return newHead.next