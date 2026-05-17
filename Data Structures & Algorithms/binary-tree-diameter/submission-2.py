# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        
        def findMaxLength(root):
            if not root:
                return 0

            l = findMaxLength(root.left)
            r = findMaxLength(root.right)

            nonlocal maxDiameter
            maxDiameter = max(maxDiameter, l + r)

            return max(l, r) + 1

        findMaxLength(root)
        return maxDiameter