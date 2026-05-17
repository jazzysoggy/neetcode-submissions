# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:            
        goodCount = 0

        mapping = {root: root.val}

        queue = deque()

        queue.append(root)

        while len(queue) > 0:
            current = queue.pop()

            if current == None:
                continue
            
            if not (current.val < mapping[current]):
                goodCount += 1
            
            mapping[current.left] = mapping[current.right] = max(current.val, mapping[current])

            queue.append(current.right)
            queue.append(current.left)

        return goodCount


            
