# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return False

        output = root.val

        def dfs(root):
            if not root:
                return 0

            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))
            nonlocal output
            output = max(output, left + right + root.val)

            return max(left, right) + root.val

        dfs(root)

        return output