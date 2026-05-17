# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return root == subRoot
        
        def same(root, subRoot):
            if not root or not subRoot:
                return root == subRoot

            return root.val == subRoot.val and same(root.left, subRoot.left) and same(root.right, subRoot.right)

        return same(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        
    