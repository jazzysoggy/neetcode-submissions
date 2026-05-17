# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__ (self):
        self.track = {}

    def height (self, root):
        if root == None:
            return 0

        if root.val in self.track:
            return self.track[root.val]

        return max(self.height(root.left), self.height(root.right)) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
            
        l = self.height(root.left)

        r = self.height(root.right)

        return self.isBalanced(root.left) and self.isBalanced(root.right) and not (l > r + 1 or r > l + 1)