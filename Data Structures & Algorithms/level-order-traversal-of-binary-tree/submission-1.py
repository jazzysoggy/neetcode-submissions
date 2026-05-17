# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []

        queue = deque()

        queue.append(root)

        while len(queue) > 0:
            output.append([])
            valid = False
            for i in range(len(queue)):
                current = queue.popleft()

                if current:
                    output[-1].append(current.val)
                    valid = True
                else:
                    continue

                queue.append(current.left)
                queue.append(current.right)
            
            if not valid:
                output.pop()

        return output
