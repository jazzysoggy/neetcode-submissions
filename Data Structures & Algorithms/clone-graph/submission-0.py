"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def recursive(node):
            
            if not node:
                return None
            nonlocal visited
            visited[node.val] = Node(node.val)

            if not node.neighbors:
                return visited[node.val]

            for neighbor in node.neighbors:
                if not neighbor.val in visited:
                    recursive(neighbor)

                visited[node.val].neighbors.append(visited[neighbor.val])

            return visited[node.val]

        return recursive(node)

        

        