# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        output = -float('inf')
        
        def dfs(root):
            if not root:
                return 0
            
            nonlocal output
            left = dfs(root.left)
            right = dfs(root.right)

            output = max(output, left + right + root.val)

            return max(max(left, right) + root.val, 0)

        dfs(root)

        return output