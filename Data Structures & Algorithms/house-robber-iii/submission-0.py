# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        maxAtPoint = {None: 0}

        def dfs(root):
            if root in maxAtPoint:
                return maxAtPoint[root]

            maxAtPoint[root] = root.val

            if root.left:
                maxAtPoint[root] += dfs(root.left.left) + dfs(root.left.right)

            if root.right:
                maxAtPoint[root] += dfs(root.right.left) + dfs(root.right.right)


            maxAtPoint[root] = max(maxAtPoint[root], dfs(root.left) + dfs(root.right))
            return maxAtPoint[root]



        dfs(root)
        return maxAtPoint[root]