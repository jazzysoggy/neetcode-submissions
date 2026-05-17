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
        if head == None:
            return None
        
        randomTracker = defaultdict(list)
        existsTracker = {}

        toReturn = Node(0)
        previous = toReturn
        while head:
            previous.next = Node(head.val)
            
            for node in randomTracker[head]:
                node.random = previous.next

            existsTracker[head] = previous.next

            if head.random in existsTracker:
                previous.next.random = existsTracker[head.random]
            else:
                randomTracker[head.random].append(previous.next)
            
            head = head.next
            previous = previous.next

        return toReturn.next
        