"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        track_item = {}

        def recurse_clone(node):
            if node in track_item:
                return

            track_item[node] = Node(node.val)

            for neighbor in node.neighbors:
                recurse_clone(neighbor)
                track_item[node].neighbors.append(track_item[neighbor])

        recurse_clone(node)

        return track_item[node]



